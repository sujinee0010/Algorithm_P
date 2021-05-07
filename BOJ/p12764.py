import sys
import heapq

n = int(sys.stdin.readline())

people = []
for i in range(n):
    start, end = map(int, sys.stdin.readline().split())
    people.append((start, end))

# 도착 시간 순 정렬
people = sorted(people, key=lambda x: x[0])
using, can_use = [], []
time, del_cnt, idx, cidx = 0, 0, 0, 1
used = dict()

while del_cnt < n:
    # 시간이 되면 삽입
    while idx < len(people) and people[idx][0] == time:
        start, end = people[idx]
        # 사용가능한 컴터 없으면
        if not can_use:
            num = cidx
            used[num] = 0
            cidx += 1
        else:
            num = heapq.heappop(can_use)

        used[num] += 1
        heapq.heappush(using, (end, start, num))
        idx += 1

    # 완료되면 삭제
    if using:
        tmp = heapq.heappop(using)
        if tmp[0] == time:
            heapq.heappush(can_use, tmp[2])
            del_cnt += 1
        else:
            heapq.heappush(using, tmp)

    time += 1

print(cidx - 1)
for us in used.values():
    print(us, end=' ')
