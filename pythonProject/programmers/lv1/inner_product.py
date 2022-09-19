def solution(a, b):
    answer = 0
    for i, j in zip(a, b):
        answer += i * j
    return answer


if __name__ == '__main__':
    print(solution([1,2,3,4], [-3,-1,0,2]))     # 3
    print(solution([-1,0,1], [1,0,-1]))     # -2
