def solution(n):
    n_list = [num for num in str(n)]
    answer = []
    for i in range(0, len(n_list)):
        answer.append(int(n_list.pop()))
    return answer


def solution2(n):
    n_list = list(map(int, reversed(str(n))))
    return n_list


if __name__ == '__main__':
    print(solution(12345))
    print(solution2(12345))
