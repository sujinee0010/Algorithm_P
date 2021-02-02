import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
INF = int(1e9) # 제한 숫자 계산 주의 하기
distance = [[100001 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    distance[a][b] = min(distance[a][b], c)

# 1 2 3 4 5 - 중간 숫자 !
for k in range(1, n + 1):
    # 시작 숫자
    for i in range(1, n + 1):
        # 끝 숫자
        for j in range(1, n + 1):
            if i == j:
                distance[i][j] =0
            else:
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
            # 2-3-1 2-4-1 2-5-1

for row in distance[1:]:
    for col in row[1:]:
        if col == int(1e9):
            print(0, end=" ")
        else:
            print(col, end=" ")
    print()
