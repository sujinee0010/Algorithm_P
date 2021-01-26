"""
dfs 돌기
종료조건은 돌은 횟수 c 되면
답 기록 조건은 최종 조합 문자가  l글자일 경우
dfs  돌떄 체 크해야되는거
- 전의 알파벳이면 안됌
- 이미 선택한 알파벳이며 안됌   --> 오름 차순 후 그 다음 인덱스부터 순회 하는 것으로 해결 가능
- 모음 하나 있는지 , 자음 두개 있는지 check
"""
import sys

l, c = map(int, sys.stdin.readline().split())
alpa = list(map(str, sys.stdin.readline().split()))

alpa.sort()

def makePWD(cnt, alpa, idx, pwd, l, c):
    if len(pwd) == l:
        m = sum(list(map(lambda x: 1 if x in pwd else 0, ['a', 'e', 'i', 'o', 'u'])))
        if m > 0 and len(pwd) - m > 1:
            print(pwd)
    else:
        for i in range(idx, len(alpa)):
            makePWD(cnt + 1, alpa, i+1, pwd + alpa[i], l, c)


makePWD(0, alpa, 0, "", l, c)