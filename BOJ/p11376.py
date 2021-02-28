import sys

n, m = map(int, sys.stdin.readline().split())

# 해당 일을 할 수 있는 사람
can = [[] for _ in range(m + 1)]

# 사람 하는 일 점유 상태 ( 초기 0 , 최대 2)
c = [0 for _ in range(n + 1)]

# 사람 기준 하는 일 기록
d = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    tmp = list(map(int, sys.stdin.readline().split()))
    for nidx in range(1, len(tmp)):
        can[tmp[nidx]].append(i)

ans = 0


def dfs(work):
    for person in can[work]:
        if c[person] == 2:
            continue
        c[person] += 1
        # 사람이 담당하고 있는 일이 2개 이해 이거나 ,
        if len(d[person]) < 2 or dfs(d[person][0]) or dfs(d[person][1]):
            d[person].append(work)
            return True
    return False


for i in range(1, m + 1):
    c = [0 for _ in range(n + 1)]
    if dfs(i):
        ans += 1

print(ans)
