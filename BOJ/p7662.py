import sys
from collections import deque
import bisect

"""
리스트 요소 삭제 - O(N)
요소 정렬 - O(NlogN)
"""
T = int(sys.stdin.readline())
result = []
for t in range(T):
    nums = dict()
    n = int(sys.stdin.readline())
    d = deque()

    for _ in range(n):
        c, number = map(str, sys.stdin.readline().split())
        # 값 삽입하기
        if c == "I":
            if nums.get(int(number)) is None:
                nums[int(number)] = 1
                bisect.insort_left(d, int(number))
            else:
                nums[int(number)] = nums.get(int(number)) + 1
        elif c == "D" and nums:
            # 최솟값 삭제하기
            if int(number) == -1:
                nums[d[0]] = nums.get(d[0]) - 1
                if nums[d[0]] == 0:
                    nums.pop(d[0])
                    d.popleft()
            # 1
            else:
                nums[d[-1]] = nums.get(d[-1]) - 1
                if nums[d[-1]] == 0:
                    nums.pop(d[-1])
                    d.pop()

    if d:
        result.append(str(d[-1]) + " " + str(d[0]))
    else:
        result.append("EMPTY")

for r in result:
    print(r)
