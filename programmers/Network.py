from collections import deque


def solution(n, computers):
    answer = 0
    visited = [False] * len(computers)
    for i in range(n):
        if not visited[i]:
            q = deque()
            q.append(i)
            while q:
                row = q.popleft()
                visited[row] = True
                for j in range(n):
                    None if i == j else q.append(j) if not visited[j] and computers[row][j] == 1 else None
            answer += 1
    return answer
