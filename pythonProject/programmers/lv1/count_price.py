def solution(price, money, count):
    answer = money

    for i in range(1, count+1):
        answer -= price * i

    if answer < 0:
        return abs(answer)
    else:
        return 0
    