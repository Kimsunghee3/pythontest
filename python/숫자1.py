import random

tries = 0
guess = 0
answer = random.randint(1, 100)

print("1부터 100 사이의 숫자를 맞추시오")
guess = int(input("숫자를 입력하시오:"))

while guess != answer:
    tries = tries + 1
    if guess < answer:
        print("낮음")
    elif guess > answer:
        print("높음!")
    guess = int(input("숫자를 입력하시오:"))

if guess == answer:
    print("축하합니다.시도횟수=", tries + 1)
else:
    print("정답은", number)
