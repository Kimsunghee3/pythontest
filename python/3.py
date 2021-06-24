# cart = ['사과', '세제', '화장지', '치약']
# if '화장지' in cart:
#     print(cart.index("화장지"))

# heroes = ["아이언맨", "토르", "헐크", "스칼렛 위치"]
# heroes.sort()
# print(heroes)

# heroes = ["아이언맨", "토르", "헐크", "스칼렛위치"]
# # new_heroes = sorted(heroes)
# # print(heroes)
# # print(new_heroes)
# # # heroes.sort(reverse=True)
# # # print(heroes)

# # num = [10, 20, 30, 40, 50, 60]
# # print(num)

# # num = [[10, 20, 30], [40, 50, 60]]
# # print(num)

# # num = [[10,20,30],[40,50,60]]
# # print(num[0][0])
# # print(num[0][1])
# # print(num[1][1])
# # num[1][2] = 100
# # print(num)

# # for i in [1, 2, 3]:
# #     print("i=", i)

# # heroes=[]

# # for i in range(5):
# #     name = input("영웅들의 이름을 입력하시오:")
# #     heroes.append(name)

# # for i in heroes:
# #     print(i,end="")
# # num = [100, 96, 209, 22, 30, 117]

# # for i in num:
# #     if i % 2 == 1:
# #         print(i, end="")

# # periodic_table = []

# # for count in range(0, 4):
# #     periodic = input("주기율표 구절을 입력하시오:")
# #     periodic_table.append(periodic)
# # print(periodic_table)

# # import random
# # quotes = []

# # quotes.append("꿈을 지녀라.그러면 어려운 현실을 이길 수 있다.")
# # quotes.append("분노는 바보들의 가슴속에서만 살아간다.")
# # quotes.append("사람은 사랑할 때 누구나 시인이 된다.")
# # quotes.append("시작이 반이다.")

# # dailyQuote = random.choice(quotes)
# # print("############################################")
# # print("#    오늘의 명언     ")
# # print("############################################")
# # print("")
# # print(dailyQuote)

# import turtle

# t = turtle.Turtle()

# # 거북이의 속도는 0으로 설정하면 최대가 됩니다.
# t.speed(0)

# # 거북이가 그리는 선의 두께는 width()를 호출합니다.
# t.width(3)

# length = 10                 # 초기 선의 길이는 10으로 합니다.

# # 색상은 리스트에 저장했다가 하나씩 꺼내서 변경하도록 합니다.
# colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']

# # while 반복문이다. 선의 길이가 500보다 작으면 반복.
# while length < 500:
#     t.forward(length)
#     t.pencolor(colors[length % 6])
#     t.right(89)
#     length += 5

import turtle
t = turtle.Turtle()
positions = [[0, 0, "green"], [-120, 0, "yellow"],
             [60, 60, "red"], [-60, 60, "black"], [-180, 60, "blue"]]
t.pensize(5)
for x, y, c in turtle.position:
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(c, c)
    t.circle(60)
