import sys

sys.setrecursionlimit(111111)  # 충분한 재귀 깊이를 주어 오류를 예방


def dfs(x):
    global result
    visited[x] = True
    cycle.append(x)  # 사이클을 이루는 팀을 확인하기 위함
    number = numbers[x]

    if visited[number]:  # 방문가능한 곳이 끝났는지
        if number in cycle:  # 사이클 가능 여부
            result += 1
        return
    else:
        dfs(number)


for _ in range(int(sys.stdin.readline())):
    N = int(int(sys.stdin.readline()))
    numbers = [0] + list(map(int , sys.stdin.readline().split()))
    visited = [True] + [False for _ in range(N)]
    result = 0

    for i in range(1,N+1):
        if not visited[i]:  # 방문 안한 곳이라면
            cycle =[]
            dfs(i) # DFS 함수 돌림

    print(result)  # 팀에 없는 사람 수
