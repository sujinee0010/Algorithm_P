
"""
-- 다익스트라
- 한 노드에서 다른 나머지 노드로 가는 최소비용을 구해야할 때 -- 시작노드(기준)가 있을때
- dp 와 우선순위큐

- dp 배열 max로 초기화하고 , 시작노드만 0으로 갱신
- 연결 그래프 [시작노드] - (도착노드 , 비용 )..
- 우선순위큐 - 비용이 적은것부터 뽑고, dp배열을 최소로 갱신한 후 갱신한 노드와 값을 우큐에 넣음

import heapq
h=[]
heapq.heappush(h , (val , node))
heapq.heappop(h)

"""


# 연결 그래프 : 시작 노드 - (도착노드 , 비용 ) , (도착노드 , 비용) ..
# 거리 기록 배열 : d[max로 초기화], 시작노드를 0으로 하기
# 우선순위큐 : 최소 비용 , 처음에 시작 노드와 비용 0 넣기

import heapq


def dijkstra(graph, start, cnt, end):
    node_list = [[] for _ in range(cnt + 1)]
    INF = int(1e9)
    d = [INF for _ in range(cnt + 1)]
    h = []
    for g in graph:
        n1, n2, val = g
        node_list[n1].append((n2, val))


    # 비용 , 노드 순 - 비용 작은순으로 정렬
    heapq.heappush(h, (0, start))
    # 시작 노드 0 으로 초기화
    d[start] = 0

    while h:
        val, n1 = heapq.heappop(h)
        for next in node_list[n1]:
            n2, nval = next
            if d[n1] + nval < d[n2]:
                d[n2] = d[n1] + nval
                heapq.heappush(h, (d[n2], n2))
    print(d)
    return d[end]

dijkstra([[1 ,2, 2],
[1 ,3 ,3],
[2 ,3 ,2],
[1 ,4 ,1],
[1 ,5 ,10],
[2 ,4 ,2],
[3 ,4 ,1],
[3 ,5, 1],
[4, 5, 3]]  , 1, 5, 5)

s =[]
heapq.heappush(s , (-0,"n1"))
heapq.heappush(s , (-1,"n1"))
heapq.heappush(s , (-2,"n1"))

while s :
    print(heapq.heappop(s))

