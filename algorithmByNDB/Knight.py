n = str(input())
x, y = int(n[1]),  ord(n[0]) - ord('a')+1

case = [(-2, -1), (-2, 1), (2, 1), (2, -1),
        (-1, -2), (1, -2), (-1, 2), (1, 2)]
ans = 0
for r, c in case:
    nx = x + r
    ny = y + c
    if 1 <= nx <= 8 and 1 <= ny <= 8:
        ans += 1

print(ans)
