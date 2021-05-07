import sys

n = int(sys.stdin.readline())
ans = n
for i in range(n):
    alpa = dict()
    word = str(sys.stdin.readline().strip())
    for widx in range(len(word)):
        if word[widx] in alpa.keys():
            if abs(alpa[word[widx]] - widx) != 1:
                ans -= 1
                break

        alpa[word[widx]] = widx

print(ans)
