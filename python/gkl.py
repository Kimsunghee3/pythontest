temp_list = [0, 10, 20, 30]
vapor_list = [4.8, 9.4, 17.3, 30.4]

temp = int(input())

if temp in temp_list:
    index = temp_list.index(temp)
    print(index)
    print(vapor_list[index])
