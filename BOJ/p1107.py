import sys


def check(number, e_buttons):
    number = str(number)
    for i in range(len(number)):
        if int(number[i]) in e_buttons:
            return False
    return True


def make_near_number(channel, e_buttons):
    # 눌리는 버튼 조합으로 가장 근접한 수를 잦는 것
    cnt = 0
    num = channel
    while True:
        # 쁠마
        min_c = channel - cnt
        max_c = channel + cnt

        # 이 수가 만들기 가능하다면
        if min_c >= 0:
            # 검사
            if check(min_c, e_buttons):
                num = min_c
                break

        if max_c >= 0:
            # 검사
            if check(max_c, e_buttons):
                num = max_c
                break

        cnt += 1

    return num


channel = int(sys.stdin.readline())
error_cnt = int(sys.stdin.readline())

if error_cnt == 0:
    print(min(abs(channel - 100), len(str(channel))))
else:
    e_buttons = list(map(int, sys.stdin.readline().split()))

    if channel == 100:
        print(0)
    elif len(e_buttons) >= 10:
        print(abs(channel - 100))
    else:
        tmp = make_near_number(channel, e_buttons)
        print(tmp)
        print(min((abs(tmp - channel) + len(str(tmp))), abs(channel - 100)))
