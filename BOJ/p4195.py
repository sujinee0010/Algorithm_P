import sys


def unionParent(n1, n2, parent):
    n1 = getParent(n1, parent)
    n2 = getParent(n2, parent)

    if n1 != n2:
        if n1 < n2:
            parent[n2] = n1
            setsize[n1] += setsize[n2]
            setsize[n2] = 0
        else:
            parent[n1] = n2
            setsize[n2] += setsize[n1]
            setsize[n1] = 0


# 동빈나꺼 찾아보자 .. 왜 리턴값에서 안돼지 바로 , 그리고 지역변수 헷갈림
def getParent(n1, parent):
    if parent[n1] == n1:
        return n1
    else:
        parent[n1] = getParent(parent[n1], parent)
        return parent[n1]


t = int(sys.stdin.readline())
result = []
for _ in range(t):
    idx = 0
    fcnt = int(sys.stdin.readline())
    parent = [i for i in range(fcnt * 2)]  # 최대 2*fcnt명
    setsize = [1 for i in range(fcnt * 2)]
    name = dict()

    for f in range(fcnt):
        f1, f2 = map(str, sys.stdin.readline().split())
        if not name or f1 not in name.keys():
            name[f1] = idx
            idx += 1
        if not name or f2 not in name.keys():
            name[f2] = idx
            idx += 1

        # 둘이 이어 준다
        unionParent(name[f1], name[f2], parent)
        result.append(setsize[getParent(name[f1], parent)])

for r in result:
    print(r)
