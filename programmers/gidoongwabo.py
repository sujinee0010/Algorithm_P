"""
기둥과 보
    -- 기둥일 경우와 보 일 경우 로 분기
    -- 설치 or 삭제 후 상태(검사 시점까지의 item) 조사 하기
"""


def isRight(result):
    for x, y, n in result:
        if n == 0:  # 기둥
            if y == 0 or ((x, y, 1) in result or (x - 1, y, 1) in result) or ((x, y - 1, 0) in result):
                pass
            else:
                return False
        elif n == 1:  # 보
            if ((x, y - 1, 0) in result or (x + 1, y - 1, 0) in result) or (
                    (x - 1, y, 1) in result and (x + 1, y, 1) in result):
                pass
            else:
                return False
    return True

def solution(n, build_frame):
    result = set()
    for x, y, n, build in build_frame:  # build_frame[:]
        item = (x, y, n)
        # 삭제
        if build == 0:
            result.remove(item)
            result.add(item) if not isRight(result) else None
        # 설치
        elif build == 1:
            result.add(item)
            result.remove(item) if not isRight(result) else None

    answer = map(list, result)
    return sorted(answer, key=lambda x: (x[0], x[1], x[2]))


# if __name__ == "__main__":
#     build_frame2 = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
#                     [2, 0, 0, 0],
#                     [1, 1, 1, 0], [2, 2, 0, 1]]
#     build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1],
#                    [3, 2, 1, 1]]
#     print(solution(5, build_frame2))
