from collections import deque

n, m = map(int, input().split())
miro = []
for i in range(n):
    miro.append(list(map(int, input())))


def miros(n, m, miro):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((0, 0))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                q.append((nx, ny))

    return miro[n - 1][m - 1]


print(miros(n, m, miro))
