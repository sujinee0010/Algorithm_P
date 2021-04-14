import sys
import copy

n = int(sys.stdin.readline())
arr = []
ans = 0
for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))


def makeArr(cnt, arr, n, s):
    ans = 0
    if cnt == 5:
        return max(map(max, arr))
    else:
        p = copy.deepcopy(arr)
        # left
        for i in range(n):
            idx = 0
            for j in range(1, n):
                tmp, p[i][j] = p[i][j], 0
                if p[i][idx] == 0:
                    p[i][idx] = tmp
                elif tmp == p[i][idx]:
                    p[i][idx] = tmp * 2
                    idx += 1
                else:
                    idx += 1
                    p[i][idx] = tmp

        ans = max(makeArr(cnt + 1, p, n, s + "-left"), ans)

        p = copy.deepcopy(arr)
        # right
        for i in range(n):
            idx = n - 1
            for j in range(n - 2, -1, -1):
                tmp, p[i][j] = p[i][j], 0
                if p[i][idx] == 0:
                    p[i][idx] = tmp
                elif tmp == p[i][idx]:
                    p[i][idx] = tmp * 2
                    idx -= 1
                else:
                    idx -= 1
                    p[i][idx] = tmp

        ans = max(makeArr(cnt + 1, p, n, s + "-right"), ans)

        p = copy.deepcopy(arr)
        # up
        for j in range(n):
            idx = 0
            for i in range(1, n):
                tmp, p[i][j] = p[i][j], 0
                if p[idx][j] == 0:
                    p[idx][j] = tmp
                elif tmp == p[idx][j]:
                    p[idx][j] = tmp * 2
                    idx += 1
                else:
                    idx += 1
                    p[idx][j] = tmp

        ans = max(makeArr(cnt + 1, p, n, s + "-up"), ans)
        p = copy.deepcopy(arr)

        # down
        for j in range(n):
            idx = 0
            for i in range(n - 2, -1, -1):
                tmp, p[i][j] = p[i][j], 0
                if p[idx][j] == 0:
                    p[idx][j] = tmp
                elif tmp == p[idx][j]:
                    p[idx][j] = tmp * 2
                    idx -= 1
                else:
                    idx -= 1
                    p[idx][j] = tmp

        ans = max(makeArr(cnt + 1, p, n, s + "-down"), ans)
        return ans


print(makeArr(0, arr, n, ""))
