import heapq
import sys

l, k, c = map(int, sys.stdin.readline().split())
h = []
for num in list(map(int, sys.stdin.readline().split())):
    heapq.heappush(h, (num))

cnt = 0
long_tree = 0
first_point = 0
point = 0
trees = []

while cnt < c:
    # 자르는 위치 2 .. 5 ...
    number = heapq.heappop(h)
    # 통나무 조각 0 -2 = 2
    tree_len = abs(point - number)
    if cnt != 1:
        first_point = number
    # 통나무 길이 , 처음 자르는 위치
    trees.append((tree_len, first_point))
    point = number # 2 .. 5..
    cnt += 1

trees.append((abs(point - l), point))
strees = sorted(trees, key=lambda x: (-x[0], x[1]))
print(strees)
print(strees[0][0], strees[0][1])
