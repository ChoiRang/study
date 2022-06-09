def solution(number, k):
    number_r = []
    for i in range(1, len(number)):
        number_r.append(number[i])
    result = [number[0]]
    for i in number_r:
        while result[-1] < i and k > 0:
            result.pop()
            k -= 1
            if not result or k <= 0:
                break
        result.append(i)

    if k > 0:
        for i in range(k):
            result.pop()

    return ''.join(result)


if __name__ == '__main__':
    print(solution('19', 1))      # 94
    print(solution('1924', 2))      # 94
    print(solution('1231234', 3))       # 3234
    print(solution('4177252841', 4))        # 775841
    print(solution('4177252841', 1))        # 477252841
    print(solution('4177252841', 3))        # 7752841
    print(solution('987654321', 5))        # 9876


# 1. 순서유지
# 2. 앞자리가 가장 큰 수(순서있는)가 될때까지 반복
# 3. k 가 0 이 되면 반복 종료
# 추가: k 값이 남는 경우의 수 존쟈
