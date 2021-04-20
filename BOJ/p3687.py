import sys
import copy

t = int(sys.stdin.readline())
# num_set = []
result = []
alpa = {2: [1], 3: [7], 4: [4], 5: [2, 3, 5], 6: [0, 6, 9], 7: [8]}


# 중복 조합
# def makeNum(idx, c, sum, nums):
#     if sum >= c:
#         if c == sum:
#             num_set.append(nums)
#     else:
#         for i in range(idx, c + 1):
#             tmp = copy.deepcopy(nums)
#             tmp.append(i)
#             makeNum(idx, c, sum + i, tmp)


def makeMaxNum(c):
    ans = ""
    if c % 2 == 0:
        for _ in range(c // 2):
            ans += '1'
    else:
        ans += '7'
        for _ in range((c - 3) // 2):
            ans += '1'
    return int(ans)


def makeMinNum(c):
    dp = [-1 for _ in range(c + 1)]
    marr = [0, 0, 1, 7, 4, 2, 0, 8]

    for i in range(c + 1):
        if i < 8:
            if i == 6:
                dp[i] = 6
            else:
                dp[i] = marr[i]
        else:
            for j in range(2, 8):
                if i - j >= 2:
                    dp[i] = min(int(str(dp[i - j]) + str(marr[j])), dp[i]) if dp[i] != -1 else int(
                        str(dp[i - j]) + str(marr[j]))

    return dp[c]


for _ in range(t):
    c = int(sys.stdin.readline())
    # 최댓값 만들기
    max_ans = makeMaxNum(c)

    # 최솟 값 만들기 
    min_ans = makeMinNum(c)
    result.append((min_ans, max_ans))

for r in result:
    print(r[0], r[1])
