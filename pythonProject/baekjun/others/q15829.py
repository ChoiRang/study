if __name__ == '__main__':
    length = int(input())
    number = input()
    answer = 0

    for i in range(length):
        answer += (ord(number[i])-96) * (31**i)
    print(answer % 1234567891)

# mod M => 문제에 나와있음, 시그마 계산후 나머지 연산해야함
