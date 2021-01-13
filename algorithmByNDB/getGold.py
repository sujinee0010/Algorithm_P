t = int(input())
result = [0]*t
for i in range(t):
    n, m = map(int, input().split())
    dp = []
    array = list(map(int, input().split()))

    arr = []
    index = 0
    for _ in range(n):
        dp.append(array[index:index + m])
        index += m

    # 열 기준
    for col in range(1, m):
        for row in range(n):
            org_num = dp[row][col]
            dp[row][col] += dp[row][col - 1]
            if row - 1 >= 0:
                dp[row][col] = max(dp[row][col], dp[row - 1][col - 1] + org_num)
            if row + 1 < n:
                dp[row][col] = max(dp[row][col], dp[row + 1][col - 1] + org_num)

    for row in range(n):
        result[i] = max(result[i], dp[row][m - 1])


for i in range(t):
    print(result[i])

