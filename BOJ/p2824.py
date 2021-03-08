import sys
from math import gcd

n = int(sys.stdin.readline())

n1 = 1
n2 = 1
for l in list(map(int, sys.stdin.readline().split())):
    n1 *= l

m = int(sys.stdin.readline())
for l in list(map(int, sys.stdin.readline().split())):
    n2 *= l

ans = str(gcd(n1, n2))
if len(ans) > 9:
    ans = ans[len(ans) - 9:]

print(ans)
