import sys
import copy


# 빈자리 채운다 -> 되는지 확인한다 -> 안돼면 끝 / 돼면 계속
def checkBox(arr, i, j):
    x = 3 if 3 <= i < 6 else 6 if 6 <= i < 9 else 0
    y = 3 if 3 <= j < 6 else 6 if 6 <= j < 9 else 0
    # 해당 구역 중복되는 넘버 있는지
    for ni in range(x, x + 3):
        for nj in range(y, y + 3):
            if ni == i and nj == j:
                continue
            if arr[ni][nj] == arr[i][j]:
                return False
    return True


def checkCol(arr, i, j):
    for row in range(9):
        if i == row:
            continue
        if arr[row][j] == arr[i][j]:
            return False

    return True


def checkRow(arr, i, j):
    for col in range(9):
        if j == col:
            continue
        if arr[i][j] == arr[i][col]:
            return False
    return True


result = []


def dfs(arr, cnt, empty_list):
    ans = 0
    if cnt == -1:
        r = copy.deepcopy(arr)
        result.append(r)
        return 1
    else:

        x, y = empty_list[cnt]

        for i in range(1,10):
            tmp = copy.deepcopy(arr)
            tmp[x][y] = i
            if checkBox(tmp, x, y) and checkCol(tmp, x, y) and checkRow(tmp, x, y):
                ans += dfs(tmp, cnt - 1, empty_list)
            if ans > 0:
                break
        return ans


"""
def dfs(arr, cnt, empty_list):
    ans = 0
    if cnt == -1:
        r = copy.deepcopy(arr)
        result.append(r)
        return 1
    else:

        x, y = empty_list[cnt]

        for i in range(1,10):
            tmp = copy.deepcopy(arr)
            tmp[x][y] = i
            if checkBox(tmp, x, y) and checkCol(tmp, x, y) and checkRow(tmp, x, y):
                ans += dfs(tmp, cnt - 1, empty_list)
            if ans > 0:
                break
        return ans

"""






arr = []
nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
for i in range(9):
    arr.append(list(map(int, sys.stdin.readline().split())))

# 빈자리 기록
empty_list = []

for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            empty_list.append((i, j))

dfs(arr, len(empty_list) - 1, empty_list)

for i in range(9):
    for j in range(9):
        print(result[0][i][j], end=' ')
    print()
