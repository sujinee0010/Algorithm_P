"""
1로 만들기 : DP
    점화식
    - Ai = min(Ai-1,Ai/2,Ai/3,Ai/5)+1
"""
num = int(input())


def makeOne(n):
    dp = [0] * 30000
    for i in range(2, n + 1):
        dp[i] = dp[i - 1]
        if i % 5 == 0:
            dp[i] = min(dp[i], dp[i // 5])
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3])
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2])
        dp[i] += 1

    return dp[n]


print(makeOne(num))
