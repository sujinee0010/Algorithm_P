import sys
"""
펠린드롬 
- dp , 자릿수 작은 것부터 (주의)
"""
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
ques = []

for _ in range(m):
    ques.append(list(map(int, sys.stdin.readline().split())))

# dp = [[False] * n] * n 이렇게 하면 안됨

dp = [[False] * n for i in range(n)]

# 한자리 두자리 체크
for i in range(n):
    dp[i][i] = True
    if i < n - 1 and nums[i] == nums[i + 1]:
        dp[i][i + 1] = True

# 3 자리수 부터 n 자리수 체크  ..
for len in range(2, n):
    for s in range(n - len):
        if nums[s] == nums[s + len] and dp[s + 1][s + len - 1] == True:
            dp[s][s + len] = True

for q in ques:
    if dp[q[0] - 1][q[1] - 1]:
        print(1)
    else:
        print(0)
