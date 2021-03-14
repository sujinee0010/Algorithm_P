import sys

n, m = map(int, sys.stdin.readline().split())
nums = []
visited = [[False] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0
for i in range(n):
    nums.append(list(map(int, sys.stdin.readline().split())))


def dfs(i, j, nums, visited):
    ans = 0
    if i == n - 1 and j == m - 1:
        return 1
    else:
        for _ in range(4):
            nx = i + dx[_]
            ny = j + dy[_]
            if 0 <= nx < len(nums) and 0 <= ny < len(nums[0]) and visited[nx][ny] == False and nums[nx][ny] < nums[i][
                j]:
                visited[nx][ny] = True
                ans += dfs(nx, ny, nums, visited)
                visited[nx][ny] = False
        return ans


visited[0][0] = True
print(dfs(0, 0, nums, visited))
