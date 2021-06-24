import random

print("주민등록번호의 성별 정보 번호를 생성합니다.")
gender = random.randrange(4)
gender = gender + 1

print("생성번호:" + str(gender))

if gender == 1 or gender == 3:
    print("남성입니다.")
else:
    print("여성입니다.")
print("프로그램을 종료합니다.")
