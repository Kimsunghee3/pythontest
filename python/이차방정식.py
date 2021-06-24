a = int(input("a값 입력:"))
b = int(input("b값 입력:"))
c = int(input("c값 입력:"))

D = b*b - 4*a*c

if D > 0:
    print("방정식의 근은 서로 다른 두 실근입니다.")
elif D == 0:
    print("방정식은 서로 같은 두 실근(중근)입니다.")
else:
    print("방정식은 서로 다른 두 허근입니다.")
