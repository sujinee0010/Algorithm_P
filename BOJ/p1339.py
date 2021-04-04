import sys

n = int(sys.stdin.readline())
words = []
alpa = []
visited = dict()
for _ in range(n):
    num = str(sys.stdin.readline()).strip()
    words.append(num)

    for i in range(len(num)):
        if num[i] not in alpa:
            alpa.append(num[i])
            visited[num[i]] = False

alpa = sorted(alpa)
num_set = []


# 0 1 2 3 4 5 6 7 8 9 - 10 개 중 alpa len 개 뽑기
def combi(choice, visited, snum):
    if choice == 0:
        if snum not in num_set:
            num_set.append(snum)
        return
    else :
        for i in range(10):
            if not visited[i]:
                # 선택
                visited[i] = True
                combi(choice - 1, visited, snum + str(i))
                visited[i] = False

print(alpa)

visited = [False for _ in range(10)]
print(visited)

combi(len(alpa), visited, "")
print(len(num_set))


