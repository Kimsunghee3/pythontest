n = int(input("값을 입력하시오:"))
even =0
odd =0

for i in range(1, n + 1):
        if i % 2 == 0:
                even = even + i
                print("짝수:",even)
        else:
                odd = odd + i
                print("홀수:",odd)

print("짝수만 더한 값:",even)
print("홀수만 더한 값:",odd)
print("모두 더한 값:" , even + odd)

