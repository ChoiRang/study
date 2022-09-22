def solution(s):
    code_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    number_list = []
    tmp_ch = []
    answer = 0
    for ch in s:
        if ch.isdigit():
            number_list.append(int(ch))
        else:
            tmp_ch.append(ch)
            tmp_str = ''.join(tmp_ch)
            if tmp_str in code_list:
                number_list.append(int(code_list.index(tmp_str)))
                tmp_ch.clear()

    number_list.reverse()

    for idx, num in enumerate(number_list):
        answer += num * 10 ** idx

    return answer


if __name__ == '__main__':
    print(solution('one4seveneight'))
    print(solution('23four5six7'))
    print(solution('2three45sixseven'))
    print(solution('123'))
