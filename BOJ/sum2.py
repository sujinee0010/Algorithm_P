import sys

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

start = 0
end = 0
sum = 0
ans = 0
while start < n or end < n:
    if sum < m and end < n:
        sum += nums[end]
        end += 1
    else:
        if sum == m:
            ans += 1
        sum -= nums[start]
        start += 1

print(ans)
