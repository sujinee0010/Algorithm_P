n = int(input())
contents = list(map(str, input().split()))

x, y = 1, 1

for c in contents:
    if c == 'L':
        y = y - 1 if 1 <= y - 1 <= n else y
    elif c == 'R':
        y = y + 1 if 1 <= y + 1 <= n else y
    elif c == 'U':
        x = x - 1 if 1 <= x - 1 <= n else x
    elif c == 'D':
        x = x + 1 if 1 <= x + 1 <= n else x


print(x, y)
