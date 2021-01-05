
"""
곱하기 혹은 더하기
그리디
- 대부분의 경우 적용되는 최고의 방법을 사용한다
- 조건이 유효한지 검사

x하기 가 +보다 더 값이 커짐
하지만 0,1 의 경우 + 하기의 경우가 더 큼 

"""
nums = input()
result = int(nums[0])

for i in range(1, len(nums)):
    num = int(nums[i])
    if result > 1 and num > 1:
        result *= num
    else:
        result += num


print(result)
