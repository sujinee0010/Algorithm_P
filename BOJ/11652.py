import sys

n = int(sys.stdin.readline())
nums = dict()
for _ in range(n):
    number = int(sys.stdin.readline())
    if number in nums.keys():
        nums[number] += 1
    else:
        nums[number] = 1

numbers = sorted(nums.keys(), key=lambda x: (-nums[x], x))
print(numbers[0])