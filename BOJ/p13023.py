import sys


def dfs(i, visited, dpth, graph):
    ans = 0
    if dpth == 4:
        return 1
    else:
        visited[i] = True
        for next in graph[i]:
            if not visited[next]:
                visited[next] = True
                ans += dfs(next, visited, dpth + 1, graph)
                # 주의 --> 방문 현황 갱신 필요
                visited[next] = False
        return ans


n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n)]

for i in range(m):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

answer = 0
for i in range(n):
    visited = [False for _ in range(n)]
    if dfs(i, visited, 0, graph) > 0:
        answer = 1
        break

print(answer)
