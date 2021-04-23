import sys

n = int(sys.stdin.readline().strip())
cnt = int(sys.stdin.readline().strip())

photo = []
like = [0 for _ in range(101)]
time = [0 for _ in range(101)]

i = 0
for num in list(map(int, sys.stdin.readline().split())):
    if num not in photo:
        if len(photo) >= n:
            rm = photo.pop()
            like[rm] = 0
        photo.append(num)
        time[num] = i

    like[num] += 1
    # 추천횟수 높은순 , 타임값 높은순
    photo = sorted(photo, key=lambda x: (-like[x], -time[x]))
    i += 1

photo = sorted(photo)
for p in photo:
    print(p, end=' ')



"""
import sys

n = int(sys.stdin.readline().strip())
cnt = int(sys.stdin.readline().strip())

photo = []
like = [0 for _ in range(101)]
time = [0 for _ in range(101)]

i = 0
for num in list(map(int, sys.stdin.readline().split())):
    # 자리가 비어있는 경우
    if not photo or len(photo) < n:
        if num not in photo:
            photo.append(num)
            time[num] = i
    # 자리가 포화된 경우
    else:
        if num not in photo:
            rm = photo.pop()
            like[rm] = 0
            photo.append(num)
            time[num] = i

    print(num)
    like[num] += 1
    # 추천횟수 높은순 , 타임값 높은순
    photo = sorted(photo, key=lambda x: (-like[x], -time[x]))
    i += 1
    print(photo)
    for p in photo:
        print('t', p , '-> ',time[p])

    print("------------")

    for p in photo:
        print('like', p, '-> ', like[p])
        
sorted(photo)


"""
