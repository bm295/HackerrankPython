import os
from datetime import datetime

import requests
from flask import Flask, request
from requests.auth import HTTPBasicAuth

# ——— Configuration ———
JIRA_DOMAIN     = "https://citigo.atlassian.net"
JIRA_EMAIL      = "EMPLAqGbXyqsWmXwWIYS8vQk"
JIRA_API_TOKEN  = "SGQgiFgl2GjFvsfPliDqvhbnLXMK0r0Y19Xqcbt4C6kTpNxrM0siHwbzd0tT1YHA"

# Comma-separated list of issue keys to process (used if INPUT_BY_JQL is False)
ISSUE_KEYS      = "FNB-69303,FNB-69298"
# Optional JQL query to fetch issue keys (used if INPUT_BY_JQL is True)
JQL_QUERY       = 'key in linkedIssues("FNB-69010") AND status != Pending'
# Choose input mode: False = use ISSUE_KEYS; True = run JQL_QUERY
INPUT_BY_JQL    = True

# Which checking logic to apply (currently only level 1 is supported)
CHECKING_LEVEL  = 1
# ————————————————————————

app = Flask(__name__)

def format_date(date_str: str) -> str:
    if not date_str:
        return "N/A"
    try:
        return datetime.strptime(date_str[:10], "%Y-%m-%d").strftime("%d-%b-%Y")
    except ValueError:
        return date_str

def fetch_json(issue_key: str) -> dict:
    url = f"{JIRA_DOMAIN}/rest/api/3/issue/{issue_key}"
    resp = requests.get(
        url,
        auth=HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN),
        headers={"Accept": "application/json"},
        timeout=10
    )
    resp.raise_for_status()
    return resp.json()

def get_basic_details(issue_key: str) -> dict:
    data = fetch_json(issue_key)["fields"]
    return {
        "key":          issue_key,
        "summary":      data.get("summary", "N/A"),
        "status":       data.get("status", {}).get("name", "N/A"),
        "due_date_dev": format_date(data.get("customfield_10118")),
        "go_live_plan": format_date(data.get("customfield_10192"))
    }

def get_keys_by_jql(jql: str) -> list:
    """Run a JQL search and return a list of issue keys."""
    url = f"{JIRA_DOMAIN}/rest/api/3/search"
    resp = requests.get(
        url,
        auth=HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN),
        headers={"Accept": "application/json"},
        params={"jql": jql, "fields": "key", "maxResults": 1000},
        timeout=10
    )
    resp.raise_for_status()
    issues = resp.json().get("issues", [])
    return [issue["key"] for issue in issues]

def get_issue_summary_status_and_links(issue_key: str, checkingLevel: int = 1) -> str:
    if checkingLevel != 1:
        return f"Checking level {checkingLevel} not supported yet."

    # Fetch root issue
    root_json = fetch_json(issue_key)
    f = root_json["fields"]
    root = {
        "key":          issue_key,
        "summary":      f.get("summary", "N/A"),
        "status":       f.get("status", {}).get("name", "N/A"),
        "due_date_dev": format_date(f.get("customfield_10118")),
        "go_live_plan": format_date(f.get("customfield_10192"))
    }

    # Collect root + linked if Pending
    issues = [root]
    if root["status"].lower() == "pending":
        for link in f.get("issuelinks", []):
            if "inwardIssue" in link:
                issues.append(get_basic_details(link["inwardIssue"]["key"]))
            elif "outwardIssue" in link:
                issues.append(get_basic_details(link["outwardIssue"]["key"]))

    # Build table
    table = (
        f"{'Key':<15}{'Summary':<40}{'Status':<15}"
        f"{'Due Date (Dev)':<20}{'Go-live Plan'}\n"
        + "-"*100 + "\n"
    )
    for i in issues:
        table += (
            f"{i['key']:<15}"
            f"{i['summary'][:37]:<40}"
            f"{i['status']:<15}"
            f"{i['due_date_dev']:<20}"
            f"{i['go_live_plan']}\n"
        )

    # If Testing Staging, count unresolved bug-subtasks
    if root["status"] == "Testing Staging":
        subtasks = f.get("subtasks", [])
        bug_subs = [
            st for st in subtasks
            if "issuetype" in st["fields"]
            and "bug" in st["fields"]["issuetype"]["name"].lower()
        ]
        total_bugs = len(bug_subs)
        unresolved = 0
        for st in bug_subs:
            cat = fetch_json(st["key"])["fields"]["status"]["statusCategory"]["name"]
            if cat != "Done":
                unresolved += 1
        table += f"\nUnresolved bugs: {unresolved}/{total_bugs}\n"

    return table

def cli_main():
    if INPUT_BY_JQL:
        keys_list = get_keys_by_jql(JQL_QUERY)
    else:
        keys_list = [k.strip() for k in ISSUE_KEYS.split(",") if k.strip()]

    for key in keys_list:
        print(f"\n=== {key} ===")
        print(get_issue_summary_status_and_links(key, checkingLevel=CHECKING_LEVEL))


@app.get("/issues")
def issues_route():
    """Return issue data for given keys or JQL."""
    jql = request.args.get("jql")
    keys = request.args.get("keys")
    if jql:
        keys_list = get_keys_by_jql(jql)
    elif keys:
        keys_list = [k.strip() for k in keys.split(",") if k.strip()]
    elif INPUT_BY_JQL:
        keys_list = get_keys_by_jql(JQL_QUERY)
    else:
        keys_list = [k.strip() for k in ISSUE_KEYS.split(",") if k.strip()]

    outputs = []
    for key in keys_list:
        table = get_issue_summary_status_and_links(key, checkingLevel=CHECKING_LEVEL)
        outputs.append(f"=== {key} ===\n{table}")

    return "<br>".join(f"<pre>{o}</pre>" for o in outputs)


@app.get("/")
def index_route():
    """Simple form allowing the user to enter a JQL query."""
    return (
        "<form action='/issues' method='get'>"
        "<input type='text' name='jql' placeholder='Enter JQL query' size='60'>"
        "<button type='submit'>Generate</button>"
        "</form>"
    )


if __name__ == "__main__":
    if os.getenv("CLI_MODE") == "1":
        cli_main()
    else:
        port = int(os.environ.get("PORT", 5000))
        app.run(host="0.0.0.0", port=port)
