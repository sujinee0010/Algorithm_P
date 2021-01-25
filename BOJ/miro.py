from collections import deque

n, m = map(int, input().split())
miro = []
for _ in range(n):
    miro.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def find_miro():
    q = deque()
    q.append([0, 0])

    while q:
        position = q.popleft()
        x = position[0]
        y = position[1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and miro[nx][ny] == 1:
                q.append([nx,ny])
                miro[nx][ny] += miro[x][y]

    return miro[n-1][m-1]

print(find_miro())
