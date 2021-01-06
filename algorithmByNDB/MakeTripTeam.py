"""
모험가 길드 (그리디)
- 공포도가 낮은 순으로 정렬 후 처리
"""
n = int(input())
people = list(map(int, input().split()))

people.sort()

result = 0
count = 0

for i in range(n):
    count += 1
    if people[i] == count:
        count = 0
        result += 1

print(result)

