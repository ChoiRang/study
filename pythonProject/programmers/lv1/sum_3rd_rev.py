def solution(n):
    base3_r = []
    answer = []
    while n != 0:
        base3_r.append(n % 3)
        n = n // 3
    for idx, num in enumerate(list(reversed(base3_r))):
        answer.append(num * 3 ** idx)

    return sum(answer)


if __name__ == '__main__':
    print(solution(45))     # 7
    print(solution(125))    # 229
