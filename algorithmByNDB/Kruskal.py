"""
-- 크루스칼

- 모든 노드를 연결하는 최소 비용 할떄 사용하는 알고리즘
- 유니온 파인드 개념을 이용한다 !
- 모든 간선을 오름차순으로 정렬한다 (class Edge)
- 사이클을 생성하는 노드가 아닌경우에(sameParent) 간선을 선택한다
- 선택한 후로는 unionParent를 통해 간선을 기록한다
- 필요한 함수와 자료형
    - Edge class - 연결노드 1, 연결노드2 , 비용 으로 구성
    - 비용 최소 순으로 간선을 정렬한 list
    - parent 배열
    - getParent , isSame( 사이클인지 확인 )
    - connect( 선택한 후 연결)

"""

def getParent(node, parent):
    if parent[node] == node:
        return node
    else:
        parent[node] = getParent(parent[node], parent)
        return parent[node]


def connect(node1, node2, parent):
    node1 = getParent(node1, parent)
    node2 = getParent(node2, parent)
    # 작은 쪽으로 갱신
    if node1 > node2:
        parent[node1] = node2
    else:
        parent[node2] = node1


def isSame(node1, node2, parent):
    if getParent(node1, parent) == getParent(node2, parent):
        return True
    else:
        return False


def kruskal(graph, parent):
    ans = 0
    edge_list = []
    for g in graph:
        n1, n2, val = g
        edge_list.append((n1, n2, val))

    # 정렬
    edge_list = sorted(edge_list, key=lambda x: x[2])

    for el in edge_list:
        n1, n2, val = el
        if not isSame(n1, n2, parent):
            connect(n1, n2, parent)
            ans += val
    print(ans)
    return ans

kruskal([[1 ,2, 5],
[1 ,3 ,4],
[2 ,3 ,2],
[2 ,4 ,7],
[3 ,4 ,6],
[3 ,5 ,11],
[4 ,5 ,3],
[4 ,6, 8],
[5, 6, 8]]  , [0,1,2,3,4,5,6])