# 수들의 합4
# 수열의 요소들이 모두 양수가 아니기 때문에, 투포인터는 쓸 수 없고,
# N이 최대 200,000이므로 O(N)으로 끝내야한다.

N, K = map(int, input().split())
L = list(map(int, input().split()))

d = {0: 1}
cnt = 0
S = 0
for i in range(N):
    S += L[i]
    print('S : ' , S , ' d : ', d)
    print('S - K : ', S - K)
    if S - K in d:
        cnt += d[S - K]
        print("s -k in d, cnt : ", cnt)
    if S in d:
        d[S] += 1
        print("s  in d, d[s] : ", d[S])
    else:
        d[S] = 1
        print("s  NOT in d, d[s] : ", d[S])

print(d)
print(cnt)