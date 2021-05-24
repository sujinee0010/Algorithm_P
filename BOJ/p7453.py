import sys
n = int(sys.stdin.readline())
alist, blist, clist, dlist = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, sys.stdin.readline().split())
    alist.append(a); blist.append(b); clist.append(c); dlist.append(d)

ab, cd = {}, {}
# 4000*4000
for a in alist:
    for b in blist:
        if not ab.get(a + b):
            ab[a + b] = 1
        else:
            ab[a + b] += 1

#4000 *4000 = 16000000
for c in clist:
    for d in dlist:
        if not cd.get(c+d):
            cd[c+d] = 1
        else: cd[c+d] += 1

ans = 0

# 16000000
for _, key in enumerate(ab):
    if cd.get(-key):
        ans += (ab[key] * cd[-key])

print(ans)
