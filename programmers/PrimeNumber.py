answerArr = set()
def isPrime(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
def dfs(cnt, numbers, snum, visited):
    size = len(numbers)
    if cnt == size and snum != "":
        answerArr.add(int(snum))
    else:
        for i in range(size):
            if not visited[i]:
                visited[i] = True
                dfs(cnt + 1, numbers, snum + numbers[i], visited)
                visited[i] = False
        if snum != "":
            answerArr.add(int(snum))
def solution(numbers):
    answer = 0
    size = len(numbers)
    visited = [False] * (size)
    dfs(0, numbers, "", visited)
    #소수의 개수 구하기
    for q in answerArr:
        if isPrime(q):
            answer += 1
    return answer


print(solution("17"))

