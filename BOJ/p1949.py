import sys

input = sys.stdin.readline
sys.setrecursionlimit(20000)

n = int(input())
w = [0] + list(map(int, input().split()))  # 인구수
graph = [[] for i in range(n + 1)]  # 연결관계

visit = [False for i in range(n + 1)]
dp = [[0] * 2 for i in range(n + 1)]


# dp[i][0]은 i정점을 포함했을때의 최댓값, dp[i][1]은 i정점을 포함하지 않았을때의 최댓값을
def dfs(start):
    visit[start] = True
    dp[start][0] = w[start]

    for next in graph[start]:
        if not visit[next]:
            dfs(next)
            dp[start][0] += dp[next][1]
            dp[start][1] += max(dp[next][0], dp[next][1])


for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)

print(max(dp[1][0], dp[1][1]))

# 참고 : https://cotak.tistory.com/29

