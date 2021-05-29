'''
아나그램이란?
서로 다른 두 문자열이 있을때 두 문자열의 알파벳을 재배열하였을때 같은 단어 혹은 문장.
예를 들어, apple과 ppale는 아나그램 abcd와 bacd는 아나그램
'''


# 문자열을 리스트로 바꾼 후, 정렬 하여 비교하는 방법 : sort - NlogN
def anagram_sort(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        # 리스트로 바꾸어 정렬
        s1, s2 = list(s1), list(s2)
        s1.sort();
        s2.sort()
        if s1 != s2:
            return False
        return True


# 문자열의 알파벳 별 사용횟수를 기록한 맵으로 비교 - iteration - N
def anagram_map(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        s1_m, s2_m = dict(), dict()
        for i in range(len(s1)):
            if s1[i] not in s1_m:
                s1_m[s1[i]] = 0
            s1_m[s1[i]] += 1
            if s2[i] not in s2_m:
                s2_m[s2[i]] = 0
            s2_m[s2[i]] += 1
        if s1_m == s2_m:
            return True
        return False


print(anagram_map('abc', 'abc'))
print(anagram_sort('abc', 'abc'))
