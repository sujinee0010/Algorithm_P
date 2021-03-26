import sys

n , m = map(int , sys.stdin.readline().split())
numbers = list(map(int , sys.stdin.readline().split()))

left = 0
right = sum(numbers)
ans=0

for num in numbers:
    left+=num
    right-=num
    ans = max(ans , left%m + right%m)

print(ans)