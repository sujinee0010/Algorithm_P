# 정렬 코드 암기하기

numbers = [10, 3, 7, 6, 5, 9, 2, 4, 4, 8, 1]
length = len(numbers)

# 버블 정렬 i 와 i+1 ,i+2 ,,, 비교
'''
for i in range(length):
    for j in range(i+1, length):
        if numbers[i]> numbers[j]:
            numbers[i] , numbers[j] = numbers[j] , numbers[i]

print(numbers)
'''
'''
# 선택 정렬 , i 와 i+1 - end 까지의 수 중의 최소값과 비교 
for i in range(length):
    min_idx = i
    for j in range(i+1, length):
        if numbers[min_idx] > numbers[j]:
            min_idx = j
    numbers[i] , numbers[min_idx] = numbers[min_idx] , numbers[i]

print(numbers)
'''

'''
# 삽입 정렬 - i 와 i-1 ~0까지의 수를 비교한다 , 단 i-1 ~0 은 이미 정렬되어있다고 가정함 
for i in range(1,length):
    for j in range(i, 0, -1):
        if numbers[j] < numbers[j-1]:
            numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
        else:
            break

print(numbers)
'''

'''
# 퀵 정렬
def quick_Sort(numbers, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and numbers[left] <= numbers[pivot]:
            left += 1
        while right > start and numbers[right] >= numbers[pivot]:
            right -= 1

        if left > right:
            numbers[right], numbers[pivot] = numbers[pivot], numbers[right]
        else:
            numbers[left], numbers[right] = numbers[right], numbers[left]
    quick_Sort(numbers, start, right - 1)
    quick_Sort(numbers, right + 1, end)


quick_Sort(numbers, 0, length - 1)
print(numbers)
'''
# 병합 정렬
