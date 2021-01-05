"""
탐욕법
- 1이 될 때 까지
- 가능하면 최대한 많이 나누는 작업
- n의 수를 급격하게 줄이면서 log시간 복잡도로 가능

"""
n, k = map(int, input().split())
cnt = 0

while True:
    # k로 나누어 떨어지는 n에 제일 근접한 정수
    target = (n // k) * k  # 48
    cnt += (n - target)  # 53 - 48 = 5  # n - 0 taget은 무조건 0 이되는 순간이 온다
    if n < k:
        break
    n = target//k
    cnt += 1
cnt -= 1
