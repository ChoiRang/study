import random
#import re
# 문자열을 입력받아 초성리스트를 반환하는 함수
lines = ""
with open("./필수사자성어.txt") as f:
  lines = f.readlines()
print(lines)
def getPronunciation(word):
  PRONUNCIATION_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
  BASE_CODE = 44032
  CHOSUNG = 588
  split_word = list(word)
  result = []

  for keyword in split_word:
    char_code = ord(keyword) - BASE_CODE
    char1 = int(char_code / CHOSUNG)
    result.append(PRONUNCIATION_LIST[char1])
  return "".join(result)

def getFamousSentence(index):
  lines = ""
  with open("필수사자성어.txt") as f:
    lines = f.readlines()
  lines = [line for line in lines if len(line.strip()) > 0]
  word = lines[index].split()[1].split("(")[0]
  hint = lines[index].split(":")[1].strip()
  return (word, hint)

def checkAnswer(userAnswer, answer):
  if userAnswer == answer:
    print("정답입니다!")
    return 1
  else:
    print("틀렸습니다!")
    return 0

randomNumber = random.randint(1, len(lines))
sentence = getFamousSentence(randomNumber)
chosung = getPronunciation(sentence[0])
print("***초성게임***")
print("아래의 초성에 해당하는 사자성어를 입력하세요.>>")
count = 0
while True:
  print("초성 :" , chosung, "힌트 :", sentence[1])
  answer = input("사자성어를 입력 : ")
  count += checkAnswer(answer, sentence[0])
  if count == 1:
    break


