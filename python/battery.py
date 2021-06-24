a = input("1번 전지가 있습니까?(Y/N)")
b = input("2번 전지가 있습니까?(Y/N)")

if a.lower() == 'y' and b.lower() == 'y':
    print("직렬연결: 전구에 불이 켜집니다.")
else:
    print("직렬연결: 전구에 불이 꺼집니다.")

if a.lower() == 'y' or b.lower() == 'y':
    print("병렬연결: 전구에 불이 켜집니다.")
else:
    print("병렬연결: 전구에 불이 꺼집니다.")
