c, b = map(int, input().split())


def dfs(s, number, cnt, sum):
    ans1, ans2, ans3 = False, False, False
    if cnt <= sum:
        if number == s and sum == cnt:
            return True
        else:
            return False
    else:
        if number - 1 >= 0:
            ans1 = dfs(s, number - 1, cnt, sum + 1)
        if number + 1 <= 200000:
            ans2 = dfs(s, number + 1, cnt, sum + 1)
        if number % 2 == 0 and 0 <= number // 2 <= 200000:
            ans3 = dfs(s, number // 2, cnt, sum + 1)

        if True in [ans1, ans2, ans3]:
            return True


move = 1
ans = 0
if c == b:
    print(0)
else:
    while c + move <= 200000:
        print(c + move, ":", move)
        if dfs(b, c + move, move, 0):
            ans = move
            print(ans)
            break
        else:
            c += move
            move += 1
