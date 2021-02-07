import sys

n = int(sys.stdin.readline())
min_arr = []
max_arr = []

for i in range(n):
    if i == 0:
        for num in list(map(int, sys.stdin.readline().split())):
            min_arr.append(num)
            max_arr.append(num)
    else:
        # 3개
        numbers = list(map(int, sys.stdin.readline().split()))
        min_arr[0] , min_arr[1], min_arr[2] = (numbers[0] + min(min_arr[0], min_arr[1])),\
                                              (numbers[1] + min(min_arr)),\
                                              (numbers[2] + min(min_arr[1], min_arr[2]))
        max_arr[0], max_arr[1], max_arr[2] = (numbers[0] + max(max_arr[0], max_arr[1])), \
                                             (numbers[1] + max(max_arr)), \
                                             (numbers[2] + max(max_arr[1], max_arr[2]))


print( max(max_arr),min(min_arr))
