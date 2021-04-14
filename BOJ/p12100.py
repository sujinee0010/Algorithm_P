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
        a = copy.deepcopy(arr)
        # right
        for i in range(n):
            idx = n - 1
            for j in range(n - 2, -1, -1):
                if a[i][j]: # 0 아닐떄 
                    temp = a[i][j]
                    a[i][j] = 0
                    if a[i][idx] == 0:
                        a[i][idx] = temp
                    elif a[i][idx] == temp:
                        a[i][idx] = temp * 2
                        idx -= 1
                    else:
                        idx -= 1
                        a[i][idx] = temp
                else:
                    print(i , j,a[i][j])

        ans = max(makeArr(cnt + 1, a, n, s + "-left"), ans)

        # left
        a = copy.deepcopy(arr)
        for i in range(n):
            idx = 0
            for j in range(1, n):
                if a[i][j]:
                    temp = a[i][j]
                    a[i][j] = 0
                    if a[i][idx] == 0:
                        a[i][idx] = temp
                    elif a[i][idx] == temp:
                        a[i][idx] = temp * 2
                        idx += 1
                    else:
                        idx += 1
                        a[i][idx] = temp
                else:
                    print(i , j)


        ans = max(makeArr(cnt + 1, a, n, s + "-right"), ans)

        # down
        a = copy.deepcopy(arr)
        for j in range(n):
            idx = n - 1
            for i in range(n - 2, -1, -1):
                if a[i][j]:
                    temp = a[i][j]
                    a[i][j] = 0
                    if a[idx][j] == 0:
                        a[idx][j] = temp
                    elif a[idx][j] == temp:
                        a[idx][j] = temp * 2
                        idx -= 1
                    else:
                        idx -= 1
                        a[idx][j] = temp
                else:
                    print(i , j)

        ans = max(makeArr(cnt + 1, a, n, s + "-up"), ans)
        a = copy.deepcopy(arr)
        #up
        for j in range(n):
            idx = 0
            for i in range(1, n):
                if a[i][j]:
                    temp = a[i][j]
                    a[i][j] = 0
                    if a[idx][j] == 0:
                        a[idx][j] = temp
                    elif a[idx][j] == temp:
                        a[idx][j] = temp * 2
                        idx += 1
                    else:
                        idx += 1
                        a[idx][j] = temp
                else:
                    print(i, j)

        ans = max(makeArr(cnt + 1, a, n, s + "-down"), ans)
        return ans


print(makeArr(0, arr, n, ""))
