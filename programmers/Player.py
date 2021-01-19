import collections


# Counter를 사용한 풀이
def solution2(participant, completion):
    print(collections.Counter(participant))
    print(collections.Counter(completion))
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(answer)
    return list(answer.keys())[0]


# 정렬 사용한 풀이
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for index in range(len(completion)):
        if completion[index] != participant[index]:
            return participant[index]
    return participant[-1]


participant = ['AA', 'BB', 'CC']
completion = ['AA', 'CC']
print(solution2(participant, completion))
