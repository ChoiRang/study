def solution(numbers, target):
    num_len = len(numbers)
    answer = 0

    def dfs(idx, result):
        if idx == num_len:
            if result == target:
                nonlocal answer
                answer += 1
        else:
            dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result-numbers[idx])
    dfs(0, 0)
    return answer
