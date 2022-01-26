import random

PRONUNCIATION_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
BASE_CODE = 44032
CHOSUNG = 588
with open("./필수사자성어.txt") as f:
  lines = f.readlines()
max_size = len([line for line in lines if len(line.strip()) > 0])


# 문자열을 입력받아 초성리스트를 반환하는 함수
def pronunciation(word):
  split_word = list(word)
  result = []

  for keyword in split_word:
    char_code = ord(keyword) - BASE_CODE
    char1 = int(char_code / CHOSUNG)
    result.append(PRONUNCIATION_LIST[char1])
  return "".join(result)


def famous_sentence(index):
  question_text = [line for line in lines if len(line.strip()) > 0]
  word = question_text[index].split()[1].split("(")[0]
  hint = question_text[index].split(":")[1].strip()
  return word, hint


def check_answer(user_answer, correct_answer):
  if user_answer == correct_answer:
    print("정답입니다!")
    return 1
  else:
    print("틀렸습니다!")
    return 0


def game():
  count = 0
  print("***초성게임***")
  print("아래의 초성에 해당하는 사자성어를 입력하세요.>>")
  while True:
    random_number = random.randint(1, max_size)
    print(random_number)
    sentence = famous_sentence(random_number)
    chosung = pronunciation(sentence[0])
    print("초성 :", chosung, "힌트 :", sentence[1])
    answer = input("사자성어를 입력 : ")
    count += check_answer(answer, sentence[0])
    if count == 1:
      break
