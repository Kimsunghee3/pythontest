import random
while True:
        x = random.randint(1,100)
        y = random.randint(1,100)
        
        print(x,'-',y,'=',end=" ")
        result = int(input(""))
        
        if result == x-y:
                print("맞았습니다.")
        
        else:
                print("틀렸습니다.")
