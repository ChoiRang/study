def solution(s):
    str_word_list = s.split(' ')
    answer = []
    for word in str_word_list:
        word_split = [i for i in word]
        str_list = []

        for idx, ch in enumerate(word_split):
            if idx % 2 == 0:
                str_list.append(str(ch).upper())
            else:
                str_list.append(str(ch).lower())
        word = ''.join(str_list)
        word.capitalize()
        answer.append(word)

    return ' '.join(answer)


if __name__ == '__main__':
    print(solution('try hello world'))
