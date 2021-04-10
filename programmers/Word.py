"""

"ba", "na", "n", "a"] 와 "banana"로 테스트 해보면
맨처음 "b"로 끝나는 단어는 없으므로 pass
다음 "a"로 끝나는 단어는 "a"와 "ba"가 있다. - "na"는 조건에 맞지 않음
"a"를 선택했을 때는 아무일도 없다. why? 처음에 b로 끝나는 단어가 없어서 값이 무한대인 상태
"ba"를 선택하면 1로 갱신해준다. - (단어 하나만으로 "ba"를 만들었다는 뜻)
다음은 "n"으로 끝나는 단어 "n"이 있다. 기존에 "ba"를 만들 때 최솟값(1개)로 만들었으므로 "n"을 추가해서 2개로 "ban"을 만든다는 뜻 | 현재 dp = [0, inf, 1, 2, ... | 맨 앞의 0은 무시
다음은 "a"으로 끝나는 단어 "a"와 "na"가 있다. - "ba"는 조건에 맞지 않음
"a" 선택: 앞에서 "ban"을 만들 때 2개(dp[3])를 썼다. "a"를 추가했으므로 이제 3개 dp = [0, inf, 1, 2, 3, ...
"na" 선택: 앞에서 "ba"를 만들 때 1개(dp[2])를 썼다. "na"를 추가했으므로 이제 2개 dp = [0, inf, 1, 2, 2, ...

"ba", "an", "nan", "ban", "n"], "banana"

[i , 1 , 1 , i,2]

"""
def solution(strs, t):
    n = len(t)
    dp = [0] * (n + 1)
    strs = set(strs)  # set을 사용하면 탐색할 때 시간복잡도 O(1)

    for i in range(1, n + 1):
        print('>> i : ', i)
        dp[i] = float('inf')  # i번째 시작시 최댓값으로 바꿔줌(최솟값 비교를 위해)
        for k in range(1, 6):
            # 인덱스 범위 때문에..
            if i - k < 0:
                s = 0
            else:
                s = i - k
            print(t[s:i])
            if t[s:i] in strs:
                dp[i] = min(dp[i], dp[i - k] + 1)
    if dp[-1] == float('inf'):
        answer = -1
    else:
        answer = dp[-1]

    return answer


solution(["ba","an","nan","ban","n"],"banana")