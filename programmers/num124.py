def solution(n):
    if n<=3:
        return '124'[n-1]
    else:
        r, m = divmod(n-1,3)
        return solution(r)+'124'[m]
'''
#124 나라의 숫자
if __name__ == "__main__":
    solution(45)
'''