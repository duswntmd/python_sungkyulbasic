#수행과제 모드 선택후 무한 계산식하기 작성일 23-11-27 연주승
import random

op=input("덧셈1, 뺄셈2, 곱셈3, 나눗셈4 (종료시 enter): ")
if op == "1":
    while True:
        n1= random.randint(1,10)
        n2= random.randint(1,10)

        n3= n1+n2
    
        print(n1,"+",n2,"의 값은? :",end="")
        mode1=input("")
        if str(mode1) =="":
            break
        if int(mode1) == n3 :
            print("정답입니다")
        else :
            print("오답입니다. 정답은",n3)
elif op == "2":
    while True:
        n1= random.randint(1,10)
        n2= random.randint(1,10)

        n3= n1-n2

        print(n1,"-",n2,"의 값은? :",end="")
        mode2=input("")
        if str(mode2)=="":
            break
        if int(mode2) == n3 :
            print("정답입니다")
        else :
            print("오답입니다. 정답은",n3)
elif op == "3":
    while True:
        n1= random.randint(1,10)
        n2= random.randint(1,10)

        n3= n1*n2
        
        print(n1,"*",n2,"의 값은? :",end="")
        mode3=input("")
        if str(mode3)=="":
            break
        if int(mode3) == n3 :
            print("정답입니다")
        else :
            print("오답입니다. 정답은",n3)
else :
    while True:
        n1= random.randint(1,10)
        n2= random.randint(1,10)

        n3= round(n1/n2,1)
        
        print(n1,"/",n2,"의 값은? :",end="")
        mode4=input("")
        if str(mode4)=="":
            break
        if round(float(mode4),1) == n3 :
            print("정답입니다")
        else :
            print("오답입니다. 정답은",n3)
    
