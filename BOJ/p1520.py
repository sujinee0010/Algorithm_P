from sys import setrecursionlimit
import sys

setrecursionlimit(10 ** 9)  # 재귀 한도 늘려주기

n, m = map(int, sys.stdin.readline().split())
nums = []
dp = [[-1] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0
for i in range(n):
    nums.append(list(map(int, sys.stdin.readline().split())))


def dfs(i, j, nums, dp):
    if i == 0 and j == 0:
        return 1
    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = 0
    for _ in range(4):
        nx = i + dx[_]
        ny = j + dy[_]
        if 0 <= nx < len(nums) and 0 <= ny < len(nums[0]) \
                and nums[nx][ny] > nums[i][j]:
            dp[i][j] += dfs(nx, ny, nums, dp)
    return dp[i][j]


print(dfs(n - 1, m - 1, nums, dp))
