import time
now = time.time()
thisYear = int(1970 + now//(365 * 24 * 3600))
age = int(input("당신의 나이를 입력하세요:"))
print("올해는" + str(age + 2050-thisYear) + "살이군요.")
