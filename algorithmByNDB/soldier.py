"""
LIS(Longest Increasing Subsequence) 알고리즘
- 가장 긴 증가하는 부분 수열

"""
n = int(input())
nums = list(map(int, input().split()))
nums.reverse()
#reversed(nums)?
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n-dp[n - 1])
