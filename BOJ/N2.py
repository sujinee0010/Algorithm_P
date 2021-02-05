import sys
import heapq
n = int(sys.stdin.readline())

h = []
for i in range(n):
    for num in map(int, sys.stdin.readline().split()):
        heapq.heappush(h, num)
    while len(h)>n:
        heapq.heappop(h)
        

print(h[0])