def checkType(s):
    if s.encode().isalpha():
        return "STRING"
    if s.isdigit():
        return "NUMBER"

    return "NONE"


st = "avbdfAp"
print(st.count('a'))
print(st.isupper())
print(st.upper())
print(st.islower())
print(st.lower())
di = dict()

di.keys()
di.values()


s1 = {1,2,3}
s2 = {3,4,5}
# 교집합
s3 = s1 & s2
print(s3)
# 합집합
s3 = s1 | s2
print(s3)
# 차집합
s3 = s1 - s2
print(s3)
# 대칭 차집합
s3 = s1 ^ s2
print(s3)
