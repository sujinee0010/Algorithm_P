"""
-- 이분매칭
- A집단이 B집단을 선택 하는 최대 방법
- 최대 몇개의 매칭을 이뤄낼 수 있는가 (만약 1인 2선택 이면 dfs를 두번씩 돌려주면됨 )
- 매칭이 가능한지 알려주는 함수 —> dfs 사용 (boolean)
- 사람 한명씩 dfs(사람 idx) 을 돌려서 return 값이 참이면 카운팅
- 필요한 것
    - 각 사람별 할 수 있는 일 기록한 리스트
    - 일 점유 여부 [일이 idx] - 해당일이 점유되었냐 아니냐 t/f - dfs돌때마다 f값으로 갱신
    - 일을 점유하고 있는 사람이 누군가 [일이 idx]

문제 : 백준 열혈강호
"""
import sys

sys.setrecursionlimit(10 ** 7)


def BipartiteMatching(pcnt, wcnt, can):
    cnt = 0
    # 일이 점유 되어있냐
    c = [False for _ in range(wcnt + 1)]
    # 일 누가 점유하고 있냐
    d = [0 for _ in range(wcnt + 1)]
    # 사람 - 할수 있는 일 (can)
    for i in range(1, pcnt + 1):
        c = [False for _ in range(wcnt + 1)]
        if dfs(i, c, d, can):
            cnt += 1
    print(cnt)
    return cnt


def dfs(pidx, c, d, can):
    for work in can[pidx]:
        if c[work]:
            continue

        c[work] = True

        if d[work] == 0 or dfs(d[work], c, d, can):
            d[work] = pidx
            return True
    return False


A, B = map(int, sys.stdin.readline().split())
graph = [[]]

for i in range(A):
    graph.append(list(map(int, sys.stdin.readline().split()))[1:])

BipartiteMatching(A, B, graph)
