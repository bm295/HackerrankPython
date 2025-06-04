import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime

# ——— Configuration ———
JIRA_DOMAIN     = "https://citigo.atlassian.net"
JIRA_EMAIL      = "minh.nb@kiotviet.com"
JIRA_API_TOKEN  = "ATATT3xFfGF0fYckRMNdzezbLNLofU1EaWQo03E7j6aOj5nD_4u6nEKL6NZn7EOxu5ZQop8Car2bPKh6V5FUAWHiLqgzAiUEZqykaC4sD2ET0JbDZcxNDpoxPzcpuFHyCXHYB6-kBW0GT3u166X9rPOddWvLBdMov2raC0h4NX_ry2dO5_Yhg6Q=171E8BCC"

# Comma-separated list of issue keys to process (used if INPUT_BY_JQL is False)
ISSUE_KEYS      = "FNB-69303,FNB-69298"
# Optional JQL query to fetch issue keys (used if INPUT_BY_JQL is True)
JQL_QUERY       = 'key in linkedIssues("FNB-69010") AND status != Pending'
# Choose input mode: False = use ISSUE_KEYS; True = run JQL_QUERY
INPUT_BY_JQL    = True

# Which checking logic to apply (currently only level 1 is supported)
CHECKING_LEVEL  = 1
# ————————————————————————

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

def main():
    if INPUT_BY_JQL:
        keys_list = get_keys_by_jql(JQL_QUERY)
    else:
        keys_list = [k.strip() for k in ISSUE_KEYS.split(",") if k.strip()]

    for key in keys_list:
        print(f"\n=== {key} ===")
        print(get_issue_summary_status_and_links(key, checkingLevel=CHECKING_LEVEL))

if __name__ == "__main__":
    main()
