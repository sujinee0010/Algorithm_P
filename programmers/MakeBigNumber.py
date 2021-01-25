def solution(number, k):
    stack = []
    for i in range(len(number)):
        while stack and k > 0 and stack[-1] < number[i]:
            stack.pop()  # 뒤부터 삭제
            k -= 1

        stack.append(number[i])
        print(stack)

    while k>0:
        stack.pop()
        k-=1

    ans = ''.join(stack)
    print(ans)
    return ans


solution("999", 2)
