import sys
import heapq

n5, n8, mix = map(int, sys.stdin.readline().split())
info = int(sys.stdin.readline())
btr = []
btr_5 = []
btr_8 = []

sum = 0
for _ in range(info):
    val, type = map(int, sys.stdin.readline().split())
    heapq.heappush(btr, (val, type))
    if type == 0:
        heapq.heappush(btr_5, (val, type))
    else:
        heapq.heappush(btr_8, (val, type))

for i in range(n5):
    if btr_5:
        sum += heapq.heappop(btr_5)

for i in range(n8):
    if btr_8:
        sum += heapq.heappop(btr_8)
