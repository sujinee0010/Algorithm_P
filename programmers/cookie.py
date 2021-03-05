def solution(cookie):
    ans = 0
    sums_cookie = []
    sum = 0
    for ck in cookie:
        sum += ck
        sums_cookie.append(sum)

    for m in range(len(cookie)):
        left = [sums_cookie[m]]
        right = []
        for i in range(len(cookie)):
            if i <= m:
                left.append(sums_cookie[m] - sums_cookie[i])
            else:
                right.append(sums_cookie[i] - sums_cookie[m])

        intersection = list(set(left).intersection(right))
        if intersection:
            ans = max(ans, max(intersection))

    print(ans)
    return ans