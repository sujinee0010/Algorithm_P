
def solution(numbers):
    numbers = list(map(str, numbers)) # 사전순... string 순 으로 ㅇㅇ
    numbers.sort(key=lambda x: x*3, reverse=True)
    #python은 int형 overflow않일어남
    return str(int(''.join(numbers)))

print(solution([1000,1000,1000 , 1000,1000,1000,1000,1000,1000]))
