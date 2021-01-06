"""
해결 아이디어
- 모든 시각의 경우를 확인한다 (완전 탐색 , Brute Forcing)
- 00시 00분 00초 부터 23시 59분 59초 까지의 경우의수 24* 60*60 = 86,400
- 모든 경우의 수를 확인해도 1초에 2000만번 수행 하는 파이썬의 경우 부담되지 않는 연산

처음 아이디어
 전체 경우의수 - 3을 포함하지 않는 경우의 수
"""

n = int(input())
count = 0
for h in range(n + 1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                count += 1
print(count)
