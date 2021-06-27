import sys
import heapq

T = int(sys.stdin.readline())
INF = int(1e9)
for _ in range(T):
    n, D, c = map(int, sys.stdin.readline().split())
    d = [INF for _ in range(n + 1)]
    com_info = [[] for _ in range(n + 1)]
    for i in range(D):
        c1, c2, s = map(int, sys.stdin.readline().split());
        com_info[c2].append([c1, s])
    h = []
    heapq.heappush(h, (0, c))
    d[c] = 0

    while h:
        sec, com = heapq.heappop(h)
        for next in com_info[com]:
            ncom, nsec = next
            if d[com] + nsec < d[ncom]:
                d[ncom] = d[com] + nsec
                heapq.heappush(h, (d[ncom], ncom))

    time, cnt = 0
    for i in range(len(d)):
        if d[i] != INF:
            time = max(time, d[i])
            cnt += 1

    print(cnt, time)
