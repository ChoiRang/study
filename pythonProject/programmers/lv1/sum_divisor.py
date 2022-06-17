def solution(left, right):
    div_len = []
    answer = 0
    for num in range(left, right+1):
        count = 0
        for i in range(1, num+1):
            if num % i == 0:
                count += 1

        if count % 2 == 0:
            answer += num
        else:
            answer -= num

    return answer


if __name__ == '__main__':
    print(solution(8, 10))
    # print(solution(13, 17))
    # print(solution(24, 27))
