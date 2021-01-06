s = input()
result = []
sum = 0

for i in s:
    if not i.isalpha():
        sum += int(i)
    else:
        result.append(i)

result.sort()
if sum != 0:
    result.append(str(sum))
# 리스트 문자열로
print(''.join(result))
