import sys

n, c = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
boxes = []
weights = [c for _ in range(n + 1)]

for _ in range(m):
    start, end, w = map(int, sys.stdin.readline().split())
    boxes.append((start, end, w))

boxes = sorted(boxes, key=lambda x: (x[1], x[0]))

sum = 0
for box in boxes:
    start, end, w = box[0], box[1], box[2]
    min_w = min(weights[start:end])
    can = w if min_w >= w else min_w

    sum += can
    for b in range(start, end):
        weights[b] -= can

print(sum)