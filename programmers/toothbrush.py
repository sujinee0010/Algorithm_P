def solution(enroll, referral, seller, amount):
    answer = []
    roots, money = dict(), dict()
    roots['-'] = 'root'

    for i in range(len(enroll)):
        money[enroll[i]] = 0
        roots[enroll[i]] = referral[i]

    for i in range(len(seller)):
        sperson = seller[i]
        samount = amount[i] * 100
        root = roots[sperson]

        # 분배
        while sperson != '-' and samount > 0:
            sub_amount = int(samount * 0.1) if int(samount * 0.1) >= 1 else 0
            money[sperson] += samount - sub_amount
            samount = sub_amount
            sperson = root
            root = roots[sperson]

    for m in money.values():
        answer.append(m)

    return answer
