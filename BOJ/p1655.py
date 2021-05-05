import sys
import heapq

# 시간 초과
n = int(sys.stdin.readline())
nums = []
answer = []
for _ in range(n):
    # 입력 숫자
    number = int(sys.stdin.readline())
    # 힙에 넣기
    heapq.heappush(nums, number)

    mid = (len(nums) - 1) // 2
    idx = 0
    nums_tmp = []
    while nums:
        del_num = heapq.heappop(nums)
        if idx == mid:
            answer.append(del_num)
        idx += 1
        nums_tmp.append(del_num)

    nums += nums_tmp


for a in answer:
    print(a)


# nums.sort()
#
# while nums:
#     print(heapq.heappop(nums))

# print(nums)
# 1 5 2 10 -99 7 5

# -99 1 2 5 5 7 10
