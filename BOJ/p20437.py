import sys

t = int(sys.stdin.readline())
result = []
for _ in range(t):

    s = str(sys.stdin.readline())
    k = int(sys.stdin.readline())

    alpa = dict()
    result3 = 100000
    result4 = 0

    for i in range(len(s)):
        if s[i] in alpa.keys():
            alpa[s[i]].append(i)
        else:
            alpa[s[i]] = [i]

        if len(alpa[s[i]]) >= k:
            result3 = min(alpa[s[i]][-1] - alpa[s[i]][-k] + 1, result3)
            result4 = max(alpa[s[i]][-1] - alpa[s[i]][-k] + 1, result4)

    if result3 == 100000 or result4 == 0:
        result.append([-1])
    else:
        result.append([result3, result4])

for r in result:
    if len(r) == 1:
        print(r[0])
    else:
        print(r[0], r[1])

