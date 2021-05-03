import sys

n = int(sys.stdin.readline())

# 나이 , 가입순
people = []
for i in range(n):
    age, name = map(str, sys.stdin.readline().split())
    people.append([i, int(age), name])

#print(people )

people = sorted(people, key=lambda x: (x[1], x[0]))

for p in people:
    print(p[1], p[2])

