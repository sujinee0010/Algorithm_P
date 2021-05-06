"""
dp - 마지막 부터 생각해보기
"""

import sys

n = int(sys.stdin.readline())
steps = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    steps[i] = int(sys.stdin.readline())

dp = [0 for _ in range(n + 1)]


for i in range(1, n + 1):
    if i < 3:
        dp[i] = dp[i-1]+steps[i]
    else:
        dp[i] = max(dp[i - 2] + steps[i], dp[i - 3] + steps[i-1] + steps[i])

print(dp[-1])
