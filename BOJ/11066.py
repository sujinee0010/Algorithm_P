import heapq
import sys

def dijkstra(files, start, cnt, end):
    node_list = [[] for _ in range(cnt + 1)]
    INF = int(1e9)
    d = [INF for _ in range(cnt + 1)]
    h = []
    for g in graph:
        n1, n2, val = g
        node_list[n1].append((n2, val))

    # 비용 , 노드 순 - 비용 작은순으로 정렬
    heapq.heappush(h, (0, start))
    d[start] = 40

    while h:
        val, n1 = heapq.heappop(h)

        for next in node_list[n1]:
            n2, nval = next
            if d[n1] + nval < d[n2]:
                d[n2] = d[n1] + nval
                heapq.heappush(h, (d[n2], n2))

    return d[end]

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    files = list(map(int , sys.stdin.readline().split()))
    graph = [[1, 2, 30], [2, 3, 30], [3, 4, 50]]

    print(dijkstra(graph, 1, 4, 4))



