def solution(s):
    list = []
    for i in range(len(s)):
        if not list and s[i] == ')':
            return False
        elif len(list) > 0:
            if list[-1] != s[i]:
                list.pop()
            else:
                list.append(s[i])
        else:
            list.append(s[i])

    if  list:
        return False
    return True
