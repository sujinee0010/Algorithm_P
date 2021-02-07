team = ["A", "B", "B", "C", "A", "A", "D", "E", "E"]

start = 0
end = 0
options = [("A", 2), ("B", 1)]
ans = 10000000000000


# 검사하는 함수
def isRight(team, options):
    for option in options:
        tname = option[0]
        tcnt = option[1]
        if team.count(tname) < tcnt:
            return False
    return True


while True:
    if isRight(team[start:end + 1], options):
        ans = min(ans, len(team[start:end + 1]))
        if start == len(team) - 1:
            break
        else:
            start += 1
    else:
        if end == len(team) - 1:
            break
        else:
            end += 1
    print(start, end)

print(ans)
