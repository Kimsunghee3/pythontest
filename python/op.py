# p = int(input("나누어지는 수를 입력하시오: "))
# q = int(input("나누는 수를 입력하시오: "))
# print("나눗셈의 몫=", p//q)
# print("나눗셈의 나머지=", p % q)

# sec = 1000
# min = sec // 60
# remainder = sec % 60
# print(min, '분', remainder, '초')

# x = y = 100
# print(x)
# print(y)

# x = 1000
# print("초깃값 x=", x)
# x += 2
# print("x += 2 후의 x=", x)
# x -= 2
# print("x -= 2 후의 x=", x)

# x = int(input("첫 번째 수:"))
# y = int(input("두 번째 수:"))
# z = int(input("세 번째 수:"))

# avg = (x + y + z) / 3
# print("평균=", avg)

# ftemp = int(input("화씨온도:"))
# ctemp = (ftemp-32)*5/9
# print("섭씨온도:", ctemp)

# x1 = int(input("x1: "))
# y1 = int(input("y1: "))
# x2 = int(input("x2: "))
# y2 = int(input("y2: "))

# print("두 점 사이의 거리=", ((x2 - x1)**2 + (y2 - y1)**2)**0.5)

# import turtle
# t = turtle.Turtle()
# t.shape("turtle")

# t.goto(0, 0)
# t.setheading(45)
# t.forward(141.4)

# t.up()
# t.goto(0, 0)
# t.down()
# t.setheading(0)
# t.forward(100)
# t.setheading(90)
# t.forward(100)

# import time

# fseconds = time.time()
# total_sec = int(fseconds)
# total_min = total_sec // 60
# minute = total_min % 60
# total_hour = total_min // 60
# hour = total_hour % 24 + 9
# print("현재 한국시간:" + str(hour) + "시" + str(minute) + "분")

money = int(input("투입한 돈: "))
price = int(input("물건가격: "))

change = money - price
print("거스름돈:", change)
coin500s = change // 500
change = change % 500

coin100s = change // 100

print("500원 동전의 개수:", coin500s)
print("100원의 동전의 개수:", coin100s)
