import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
numbers = []

for _ in range(n):
    numbers.append(int(sys.stdin.readline()))
# numbers = list(map(int, sys.stdin.readline().split()))

#print(numbers)
num_set = []


def make_Set(i, st, limit, numbers, visited):
    if i == limit:
        if st not in num_set:
            num_set.append(st)
            #print(st)
    else:
        for ni in range(len(numbers)):
            if not visited[ni]:
                visited[ni] = True
                make_Set(i + 1, st + str(numbers[ni]), limit, numbers, visited)
                visited[ni] = False


v = [False for _ in range(n)]
make_Set(0, '', k, numbers, v)
print(len(num_set))
