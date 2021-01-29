import heapq
import sys

INF = int(1e9)
v, e = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
num_list = [[] for _ in range(v+1)]


for _ in range(e):
    S, E, V = map(int, sys.stdin.readline().split())
    num_list[S].append([E, V])

distance = [INF] * (v + 1)
distance[start] = 0

h = []
heapq.heappush(h, (0, start))

while h:
    node_dis , start_node = heapq.heappop(h)
    for next in num_list[start_node]:
        end_node = next[0]
        val = next[1]
        if distance[end_node] > distance[start_node] + val:
            distance[end_node] = distance[start_node] + val
            heapq.heappush(h, (distance[end_node], end_node))

for i in range(1, len(distance)):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
