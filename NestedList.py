students = list()
n = int(raw_input())
for _ in range(n):
    name = raw_input()
    score = float(raw_input())
    students.append([name, score])

scores = set([students[i][1] for i in range(n)])
scores = list(scores)
scores.sort()

students = [i[0] for i in students if i[1] == scores[1]]
students.sort()

for s in students:
    print s
