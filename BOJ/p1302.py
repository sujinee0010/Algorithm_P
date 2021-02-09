import sys

n = int(sys.stdin.readline())

books = dict()
for _ in range(n):
    name = str(sys.stdin.readline().split())
    if name in books.keys():
        books[name] += 1
    else:
        books[name] = 1

titles = books.keys()
titles = sorted(titles, key=lambda x: (-books[x], x))
print(titles[0].replace("['", "").replace("']", ""))
