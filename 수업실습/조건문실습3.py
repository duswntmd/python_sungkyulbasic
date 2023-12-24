#조건문실습3-1
#F학점 여부 출력 (점수가 60점 미만이거나 결석회수가 4번이상이면 F학점 출력)
score=int(input("본인 점수를  입력"))
absent=int(input("결석회수 입력"))

if score>=90 and absent<4:
    print("A학점 입니다.")
elif score>=80 and absent<4:
    print("B학점 입니다.")
elif score>=70 and absent<4:
    print("C학점 입니다.")
elif score>=60 and absent<4:
    print("D학점 입니다.")
else:
    print("F학점 입니다.")
