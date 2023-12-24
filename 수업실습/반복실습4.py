import random
op=input("덧셈 1, 뺄셈2, 곱셈 3, 나눗셈4,")


while True:
    a = random.randint(1, 10)
    b = random.randint(1, 10)

    if op =="1":

    print(a,"+",b,"=",end="")
    ans=(input(""))
    if (ans)=="":
        break
    if int(ans) == a+b:
        print("정답입니다.")
    else:
        print("틀렸습니다. 정답은", a+b)





'''
s=0
while True:
     num=int(input("정수 입력:"))
     s=s+num
     if num==0:
         break
print("합계", s)
'''
