import heapq
import sys


n, m = map(int, sys.stdin.readline().split())
cnt = [0] * (n + 1)
info = [[] for _ in range(n + 1)]
result = []

for _ in range(m):
    n1, n2 = map(int, sys.stdin.readline().split())
    info[n1].append(n2)
    cnt[n2] += 1


h = []


for i in range(1, len(cnt)):
    if cnt[i] == 0:
        heapq.heappush(h, i)

while h:
    p = heapq.heappop(h)
    result.append(p)

    for next in info[p]:
        cnt[next] -= 1
        if cnt[next] == 0:
            heapq.heappush(h,next)

for r in result:
    print(r, end=' ')
