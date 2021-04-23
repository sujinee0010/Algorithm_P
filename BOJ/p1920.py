import sys

n = int(sys.stdin.readline())
result =[]
nums = dict()
for num in list(map(int , sys.stdin.readline().split())):
    nums[num]=0

m = int(sys.stdin.readline())

for mnum in list(map(int , sys.stdin.readline().split())):
    if mnum in nums.keys():
        result.append(1)
    else:
        result.append(0)

for r in result:
    print(r)