import sys

n = int(sys.stdin.readline())
line = str(sys.stdin.readline().strip())


# 정수는 모두 0보다 크거나 같고, 9보다 작거나 같다
# 3 + 8 * 7 - 9 * 2
# 0 1 2 3 4 5 6 7 8  -> 연산자 4  / 숫자  5

# 8 * 3 + 5
# 0 1 2 3 4 -> 연산자 2 / 숫자 3

# 8 * 3 + 5 + 2
# 0 1 2 3 4 5 6 -> 연산자 3 / 숫자 4

# 연산자는 홀수에 있다

# 괄호 치는거 재귀로 ..

def makeLine(line):
    ans = 0
    if len(line) == 1:
        return int(line)
    else:
        for i in range(len(line)):
            print(i , line)
            # 연산자 일떄
            if line[i] in ['+', '*', '-']:
                num1 = line[i-1]
                # 두자리 숫자
                if i-2 >= 0 and line[i-2] not in ['+', '*', '-']:
                    num1 = line[i-2]+num1

                op = line[i]
                # 다음숫자
                next = line[i + 2]
                new_num = 0
                if op == '+':
                    new_num = int(line[i]) + int(next)
                if op == '-':
                    new_num = int(line[i]) - int(next)
                if op == '*':
                    new_num = int(line[i]) * int(next)

                new_line = line[:i] + str(new_num) + line[i + 3:]

                ans = max(ans, makeLine(new_line))
        return ans


print(makeLine(line))
