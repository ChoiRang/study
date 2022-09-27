def solution(numbers):
    answer = []
    for idx_1, enum_1 in enumerate(numbers):
        for idx_2, enum_2 in enumerate(numbers):
            sum_enum = enum_1 + enum_2
            if idx_1 != idx_2 and sum_enum not in answer:
                answer.append(sum_enum)
    answer.sort()
    return answer


if __name__ == '__main__':
    print(solution([2,1,3,4,1]))        # [2,3,4,5,6,7]
    print(solution([5,0,2,7]))      # [2,5,7,9,12]
