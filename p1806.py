# import sys
#
# n, m = map(int, sys.stdin.readline().split())
#
# s, e = 0, 1
# ans = int(1e9)
# numbers = list(map(int, sys.stdin.readline().split()))
# sums = []
# nsum = 0
# for num in numbers:
#     nsum += num
#     sums.append(nsum)
#
# while s < len(numbers) or e < len(numbers):
#
#     if sums[e] - sums[s] >= m:
#         if sums == m:
#             ans = min(ans, abs(s - e) + 1)
#         sums -= numbers[s]
#         s += 1
#     else:
#         if e == len(numbers) - 1:
#             s += 1
#
#         else:
#             sums += numbers[e]
#
# if ans == int(1e9):
#     print(0)
# else:
#     print(ans)
N, S = map(int, input().split())
A = list(map(int, input().split()))

# 먼저 0~n까지의 합을 구해줌
sum_A = [0] * (N + 1)
for i in range(1, N + 1):
    sum_A[i] = sum_A[i - 1] + A[i - 1]

# 투포인터 설정
answer = 1000001
start = 0
end = 1

# 알고리즘 실행
while start != N:
    if sum_A[end] - sum_A[start] >= S:
        answer = min(answer, abs(end - start))
        start += 1
    else:
        if end != N:
            end += 1
        else:
            start += 1

# 답이 없을 경우 & 있을 경우
if answer != 1000001:
    print(answer)
else:
    print(0)
