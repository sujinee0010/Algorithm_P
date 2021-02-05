import sys

n, m = map(int, sys.stdin.readline().split())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))

nums.sort()

start = 0
end = 1
sub = 0
ans = sys.maxsize
while start < n and end < n:

    sub = nums[end] - nums[start]

    if sub < m:
        end += 1
    else:
        ans = min(ans, sub)
        start += 1

print(ans)
