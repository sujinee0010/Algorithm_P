"""
-- 유니온 파인드

- parent 배열로 부모 노드 기록
- 구현함수 3 개 - connect , isSame , getParent
- connect - 연결해주는 함수
- isSame - 부모가 같은지 확인
- getParent - 재귀호출을 통해서 부모노드를 가져옴
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
