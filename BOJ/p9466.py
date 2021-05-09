import sys

sys.setrecursionlimit(111111)  # 충분한 재귀 깊이를 주어 오류를 예방


def dfs(x):
    global result
    visited[x] = True
    cycle.append(x)  # 사이클을 이루는 팀을 확인하기 위함
    number = numbers[x]

    if visited[number]:  # 방문가능한 곳이 끝났는지
        if number in cycle:  # 사이클 가능 여부
            result += cycle[cycle.index(number):]  # 사이클 되는 구간 부터만 팀을 이룸
        return
    else:
        dfs(number)


for _ in range(int(input())):
    N = int(input())
    numbers = [0] + list(map(int, input().split()))
    visited = [True] + [False] * N  # 방문 여부
    result = []

    for i in range(1, N + 1):
        if not visited[i]:  # 방문 안한 곳이라면
            cycle = []
            dfs(i)  # DFS 함수 돌림

    print(N - len(result))  # 팀에 없는 사람 수


# import sys
# from collections import deque
#
#
# # 사이클을 이루는 걸 찾기
#
# def bfs(num, graph, visited):
#     q = deque()
#     q.append(num)
#     ans = []
#     while q:
#         student = q.popleft()
#         ans.append(student)
#         visited[student] = True
#
#         if not visited[graph[student][0]]:
#             q.append(graph[student][0])
#         else:
#             # 자기 자신일 경우
#             if student == graph[student][0]:
#                 return [student]
#             # 사이클일 경우
#             elif graph[student][0] == num:
#                 return ans
#             # 아무것도 아닐경우
#             else:
#                 return []
#
#
# t = int(sys.stdin.readline())
# answer = []
# for _ in range(t):
#     cnt = int(sys.stdin.readline())
#     graph = [[] for _ in range(cnt + 1)]
#     idx = 1
#     for num in list(map(int, sys.stdin.readline().split())):
#         graph[idx].append(num)
#         idx += 1
#
#     # 사이클 찾기
#     used = [1 for _ in range(cnt + 1)]
#
#     for i in range(1, cnt + 1):
#         visited = [False for _ in range(cnt + 1)]
#         if not visited[i]:
#             for s in bfs(i, graph, visited):
#                 used[s] = 0
#     #print(used)
#     answer.append(sum(used)-1)
#
# for a in answer:
#     print(a)

#
