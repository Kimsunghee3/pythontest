import random
score = 0

while True:
    room = random.randint(1, 3)
    n = int(input("방번호를 입력하세요:"))

    if n == room:
        print("범인체포!")
        score += 100
        break

    elif n > 3:
        print(n, "번방은 없습니다.")

    else:
        print("범인이 없습니다.")
        score -= 10

print("게임종료")
print("점수:", score, "점")
