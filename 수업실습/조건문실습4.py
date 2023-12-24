#조건문실습4
import random
a=random.randint(1,10)
b=random.randint(1,10)
print(a,"+",b,"=", end="")
c=int(input(""))
if c == a+b:
    print("정답입니다.")
else:
    print("오답입니다.", a+b)
