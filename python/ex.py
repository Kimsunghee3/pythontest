# age
import random
age = 20
if age < 20:
    print("20살 미만")
else:
    print("20살 이상")

# No.2
age = 20
if age < 30 and 50:
    print("30이상 50이하")
else:
    print("30미만 50이상")

# No.3
score = int(input("성적을 입력하시오:"))

if score >= 90:
    print("A학점입니다.")
elif score >= 80:
    print("B학점입니다.")
elif score >= 70:
    print("C학점입니다.")
elif score >= 60:
    print("D학점입니다.")
else:
    print("F학점입니다.")

# weather
temp = int(input("현재온도를 입력하세요:"))

if temp >= 25:
    print("반바지를 추천합니다.")
else:
    print("긴바지를 추천합니다.")
