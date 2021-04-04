import sys
from collections import deque

arr = [[] for _ in range(5)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 배열 채우기
for i in range(5):
    line = str(sys.stdin.readline().strip())
    for j in range(len(line)):
        arr[i].append(line[j])

# 좌표 총 모음
xy_set = []
for i in range(5):
    for j in range(5):
        xy_set.append((i, j))


# 자리 연결 여부 확인
def isconnect(choice_list):
    q = deque()
    q.append(choice_list[0])
    used = [choice_list[0]]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and (nx, ny) in choice_list and (nx, ny) not in used:
                q.append((nx, ny))
                used.append((nx, ny))

    if len(used) == 7:
        return True
    else:
        return False


# 자리 25개 중에 7개 뽑기
def select(xy_set, depth, choice_list, member):
    ans = 0
    # 7자리 뽑은거
    if len(choice_list) == 7:
        if member.count('S') >= 4 and isconnect(choice_list):
            return 1
        return 0
    if depth == 25:
        return 0
    else:
        x = xy_set[depth][0]
        y = xy_set[depth][1]
        choice_list.append(xy_set[depth])
        ans += select(xy_set, depth + 1, choice_list, member + arr[x][y])

        choice_list.remove(xy_set[depth])
        ans += select(xy_set, depth + 1, choice_list, member)
        return ans


# 25 개중에 7자리 뽑는다
print(select(xy_set, 0, [], ""))
