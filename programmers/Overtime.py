import heapq


def solution(n, works):
    for _ in range(len(works)):
        works[_] *= -1
    heapq.heapify(works)
    while n > 0:
        number = heapq.heappop(works)  # -1
        if number < 0:
            number += 1  # 빼준다
        heapq.heappush(works, number)
        n -= 1

    answer = 0
    while len(works) > 0:
        m = heapq.heappop(works)
        answer += pow(m * -1, 2)
    return answer
