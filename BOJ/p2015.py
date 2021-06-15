"""
수들의 합4
수열의 요소들이 모두 양수가 아니기 때문에, 투포인터는 쓸 수 없고,
N이 최대 200,000이므로 O(N)으로 끝내야한다.

S - K = X 는 i에서부터 j까지의 구간합이 K인지 구하는것
S - X = K 인 수 가 있느냐

S = j까지의 합
X = i까지의 합
-> i ~ j 까지의 구간합이 K인 수가 있으면 정답을 기록하겠다

"""

N, K = map(int, input().split()) # 4, 0
L = list(map(int, input().split()))

d = {0: 1}
cnt = 0
S = 0
for i in range(N):
    S += L[i]
    if S - K in d:
        cnt += d[S - K]
    # 누적합 기록
    if S in d:
        d[S] += 1
    else:
        d[S] = 1

print(cnt)