import sys
import heapq

n5, n8, mix = map(int, sys.stdin.readline().split())
info = int(sys.stdin.readline())
btr = []
btr_5 = []
btr_8 = []
cnt=0
sum = 0
for _ in range(info):
    val, type = map(int, sys.stdin.readline().split())
    if type == 0:
        heapq.heappush(btr_5, (val, type))
    else:
        heapq.heappush(btr_8, (val, type))

for i in range(n5):
    if btr_5:
        cnt+=1
        sum += heapq.heappop(btr_5)[0]

for i in range(len(btr_5)):
    val ,type = btr_5[i]
    heapq.heappush(btr,(val,type))


for i in range(n8):
    if btr_8:
        cnt+=1
        sum += heapq.heappop(btr_8)[0]

for i in range(len(btr_8)):
    val ,type = btr_8[i]
    heapq.heappush(btr,(val,type))

for i in range(mix):
    if btr:
        cnt+=1
        sum += heapq.heappop(btr)[0]


print(cnt , sum)
