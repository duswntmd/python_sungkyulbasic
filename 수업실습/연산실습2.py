#실습2

score = int(input("점수 입력: "))
absence = int(input("결석 횟수 입력: "))
print("F학점 여부 = ", score < 60 or absence >= 4 )
