import sys

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    parent = [0 for _ in range(n + 1)]  # 각 노드의 부모노드 저장

    for i in range(n - 1):
        p, c = map(int, sys.stdin.readline().split())
        parent[c] = p

    a, b = map(int, sys.stdin.readline().split())
    a_parents = [a]
    b_parents = [b]

    # 루트 노드들 기록하기
    while parent[a]:
        a_parents.append(parent[a])
        a = parent[a]

    while parent[b]:
        b_parents.append(parent[b])
        b = parent[b]

    aidx = len(a_parents) - 1
    bidx = len(b_parents) - 1

    # 루트노드가 달라질떄까지 검사
    while a_parents[aidx] == b_parents[bidx]:
        aidx -= 1
        bidx -= 1
    print(a_parents[aidx+1])



