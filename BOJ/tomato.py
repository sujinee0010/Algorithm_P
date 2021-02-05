from collections import deque
import sys

# 열, 행 , 층
m, n, h = map(int, sys.stdin.readline().split())
boxes = []
for __ in range(h):
    boxes.append([])
    for _ in range(n):
        boxes[__].append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()

# 안익은 토마토 1개라도 있으면 t
flag = False


# 익은 토마토 좌표 기록하기 층 , 행 , 열
def checkTomato():
    global flag
    for box in range(len(boxes)):
        for row in range(len(boxes[box])):
            for col in range(len(boxes[box][row])):
                if boxes[box][row][col] == 0:
                    flag = True
                if boxes[box][row][col] == 1:
                    q.append([box, row, col])


# 토마토 익히기
def make_tomato():
    # 익은 토마토 1도 없는 경우
    if not q:
        return -1
    # 처음부터 다 익어 있는 경우
    if not flag:
        return 0

    date = 0
    while q:
        position = q.popleft()
        b = position[0]  # 층
        x = position[1]  # 행
        y = position[2]  # 열
        date = max(date, boxes[b][x][y])
        # 같은 층 상하 좌우
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and boxes[b][nx][ny] == 0:
                q.append([b, nx, ny])
                boxes[b][nx][ny] = boxes[b][x][y] + 1

        if b - 1 >= 0 and boxes[b - 1][x][y] == 0:
            q.append([b - 1, x, y])
            boxes[b - 1][x][y] = boxes[b][x][y] + 1

        if b + 1 < h and boxes[b + 1][x][y] == 0:
            q.append([b + 1, x, y])
            boxes[b + 1][x][y] = boxes[b][x][y] + 1

    # 토마토 검사 밭에  0 이 있는 경우 :: -1

    for box in range(len(boxes)):
        for row in range(len(boxes[box])):
            for col in range(len(boxes[box][row])):
                if boxes[box][row][col] == 0:
                    return -1

    return date - 1


checkTomato()
print(make_tomato())
