'''
2, 3, 5
소수 : 약수가 1과 자기 자신 밖에 없는 2 이상의 자연수

에라토스테네스의 체
루트 돌리는

'''
n = 100
arr = [True] * (n + 1)

for i in range(2, n + 1):
    if arr[i]:
        print(i)  # 소수인 경우
        j = i
        while j <= n:
            arr[j] = False
            j += i
