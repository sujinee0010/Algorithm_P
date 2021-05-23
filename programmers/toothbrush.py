def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    roots, money = dict(), dict()
    roots['-'] = 'root'

    for i, name in enumerate(enroll):
        money[name] = i
        roots[name] = referral[i]

    for i in range(len(seller)):
        sperson = seller[i]
        samount = amount[i] * 100
        root = roots[sperson]
        while sperson != '-' and samount > 0:
            sub_amount = int(samount * 0.1) if int(samount * 0.1) >= 1 else 0
            answer[money[sperson]] += samount - sub_amount
            samount = sub_amount
            sperson = root
            root = roots[sperson]

    return answer