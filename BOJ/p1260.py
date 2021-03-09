import sys
from collections import deque

n, m, start = map(int, sys.stdin.readline().split())

visited = [False for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
    graph[n1] = list(set(graph[n1]))
    graph[n2] = list(set(graph[n2]))


def dfs(start, visited, graph):
    visited[start] = True
    graph[start].sort()
    print(start, end=' ')
    for num in graph[start]:
        if not visited[num]:
            visited[num] = True
            dfs(num, visited, graph)


def bfs(start, visited, graph):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        number = q.popleft()
        print(number, end=' ')
        graph[number].sort()
        for node in graph[number]:
            if not visited[node]:
                visited[node] = True
                q.append(node)


dfs(start, visited, graph)
visited = [False for _ in range(n + 1)]
print()
bfs(start, visited, graph)
