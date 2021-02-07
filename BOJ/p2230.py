import sys

n, m = map(int, sys.stdin.readline().split())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))

start = 0
end = 1
ans = sys.maxsize
nums.sort()
while True:

    sub = nums[end] - nums[start]

    if sub >= m:
        ans = min(ans, sub)
        if sub == m or start == n - 2:
            break
        start += 1
    else:
        if end == n - 1:
            break
        end += 1
print(ans)
