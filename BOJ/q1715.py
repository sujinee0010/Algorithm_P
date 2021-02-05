# 우선순위큐
import sys
import heapq

n = int(sys.stdin.readline())
h = []

for _ in range(n):
    heapq.heappush(h, int(sys.stdin.readline()))

ans = 0

while h and n > 1:
    n1 = heapq.heappop(h)
    n2 = heapq.heappop(h)
    ans += n1 + n2
    print(ans)
    if not h:
        break
    heapq.heappush(h, n1 + n2)

print(ans)
