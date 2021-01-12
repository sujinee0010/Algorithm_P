"""
점화식
[k원, s원 ..]
- Ai = min( Ai-k + 1 , Ai-s+1,...)

"""

n, m = map(int, input().split())
# N개의 화폐 단위 정보를 입력 받기
array = []
for i in range(n):
    array.append(int(input()))

sorted(array)

dp = [10001] * (m + 1)

for money in array:
    dp[money] = 1

for i in range(1, m + 1):
    for j in range(len(array)):
        if array[j] > i:
            continue
        if dp[i - array[j]] != 10001:
            dp[i] = min(dp[i], dp[i - array[j]] + dp[array[j]])

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])
