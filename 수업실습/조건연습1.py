#조건연습1

speed = int(input("현재 속도 입력(km/h):"))

if speed >=40 and speed < 80 :
    print(speed, "는 정상속도입니다.")
elif speed < 40:
    print(speed,"는 저속입니다.")
else:
    print(speed,"는 고속입니다.")
