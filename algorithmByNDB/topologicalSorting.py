"""
-- 위상정렬

- 그래프 탐색에 순서가 있는경우 (사이클 x)
- 간선 그래프 / 진입차수 기록 배열 / 큐를 사용해서 진입차수가 0인것을 뽑는다

- 시작 노드 연결된 노드 의 진입차수를 -1 하고
- 진입차수가 0 일 경우 , 큐에 삽입

"""


from collections import deque
import sys

def topologicalSorting(orders, cnt):
    d = [0 for _ in range(cnt + 1)]
    graph = [[] for _ in range(cnt + 1)]
    for o in orders:
        n1, n2 = o
        graph[n1].append(n2)
        d[n2] += 1

    q = deque()
    for i in range(1,len(d)):
        if d[i] == 0:
            q.append((i))


    while q:
        node = q.popleft()
        print(node , end=' ')

        for next in graph[node]:
            d[next] -= 1
            if d[next] == 0:
                q.append(next)


n , m = map(int, sys.stdin.readline().split())
arr =[]
for i in range(m):
    arr.append(list(map(int ,sys.stdin.readline().split())))

topologicalSorting(arr,n)