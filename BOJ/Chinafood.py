import sys

n, m = map(int, sys.stdin.readline().split())
foods = list(map(int, sys.stdin.readline().split()))

num = 1
for food in foods:
    min_dis = min(abs(num - food), abs(n - (abs(num - food))))
    print(min_dis , end= ' ')
    num = food


