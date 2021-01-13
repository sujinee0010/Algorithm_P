t = int(input())

result = []

for i in range(t):
    n , m = map(int , input().split())
    nums = list(map(int ,input().split()))

    arr =[]

    for i in range(len(nums)):
        row =[]
        for j in range(m): # 4 개씩 자른다 ?
            row.append(nums[i])
    dp =[]
    # 열 기준
    for i in range(m):
        for j in range(n):
            dp[i] = max(p[i-1]+ arr[j][i])

