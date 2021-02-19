import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
result = []
info = [[] for _ in range(n + 1)]
cnt = [0 for _ in range(n + 1)]

for _ in range(m):
    n1, n2 = map(int, sys.stdin.readline().split())
    info[n1].append(n2)  # 연결 관계
    cnt[n2] += 1


q = deque()

for i in range(1, len(cnt)):
    if cnt[i] == 0:
        q.append(i)


while q:
    student = q.pop()
    result.append(student)
    # 연결된 간선 삭제 - 여기서 다음 삽입 노드 선택 (안하면 시간초과)-> 방문 처리 따로 필요 x
    for next in info[student]:
        cnt[next]-=1
        if cnt[next] ==0:
            q.append(next)

for i in result:
    print(i, end=' ')

