"""
첫번째 or 두번째


"""

import sys

n = int(sys.stdin.readline())
steps = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    steps[i] = int(sys.stdin.readline())


def make_step(steps, sum, n, cnt):
    ans = 0
    if n == 0:
        return sum
    else:
        # 한칸 뛰기
        if cnt < 2 or n == 1:
            ans = max(ans , make_step(steps, steps[n - 1] + sum, n - 1, cnt + 1))

        # 두칸 뛰기
        if n - 2 >= 0:
            ans = max(ans ,make_step(steps, steps[n - 2] + sum, n - 2, 1))
        return ans


print(make_step(steps, steps[n], n, 1))
