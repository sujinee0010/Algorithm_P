def solution(people, limit):
    answer = 0
    people.sort(reverse=True)

    f = 0
    e = len(people) - 1

    while f < e:
        sum = people[f] + people[e]
        if sum > limit:
            f += 1
        else:
            f += 1
            e -= 1
        answer += 1

    if f == e:
        answer += 1

    return answer

people = [70, 50, 80]

print(solution(people, 100))
