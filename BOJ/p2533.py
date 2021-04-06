import sys

n = int(sys.stdin.readline())
# 그래프 연결관계
graph = [[_] for _ in range(n + 1)]
for _ in range(n - 1):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

# 연결된 노드 많은 순으로 정렬
graph = sorted(graph, key=lambda x: -len(x))
cnt = 0
used_num = []

# 연결된 노드 기록 하며 카운팅
for g in graph:
    if g[0] == 0:
        break
    tmp = used_num
    used_num = list(set(used_num + g))
    if tmp != used_num:
        print(used_num)
        cnt += 1

print(cnt)
