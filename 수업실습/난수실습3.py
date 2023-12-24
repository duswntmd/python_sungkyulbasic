import random

n = random.randint(1,100)

num=int(input("1~100 사이의 수를 맞춰보세요:"))

while n != num:

    if n < num:
        print("난수값은 더 작은 수 입니다.")
    else :
        print("난수값은 더 큰 수 입니다.")
        
    num=int(input("다시 입력하세요:"))
print("맞췄습니다. 난수의 값은", n)
