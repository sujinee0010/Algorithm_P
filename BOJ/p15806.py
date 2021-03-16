import sys
from collections import deque

n, m, k, t = map(int, sys.stdin.readline().split())
room = [[0] * (n + 1) for _ in range(n + 1)]  # 이거 !!!
gom_point = deque()
check_point = []

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    room[i][j] = 1
    gom_point.append((i, j))

for _ in range(k):
    i, j = map(int, sys.stdin.readline().split())
    check_point.append((i, j))

for day in range(t):
    next_gom = []
    while gom_point:
        # 곰팡이 좌표
        x, y = gom_point.popleft()
        # 곰팡이 없애기
        room[x][y] -=1
        # 곰팡이 퍼뜨리기
        for _ in range(8):
            nx = x + dx[_]
            ny = y + dy[_]
            if 1 <= nx <= n and 1 <= ny <= n:
                room[nx][ny] += 1
                next_gom.append((nx, ny))

    for gom in next_gom:
        gom_point.append(gom)

ans = 'NO'

for point in check_point:
    x, y = point
    if room[x][y] == 1:
        ans = 'YES'

print(ans)
