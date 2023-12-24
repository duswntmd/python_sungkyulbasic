speed = int(input("도로의 규정 속도를 입력(km/m):"))
mycar = int(input("내 차의 속도를 입력(km/m):"))

if mycar <= speed * 1.05:
    print("정상속도")
elif mycar > speed * 1.05 and mycar <= speed * 1.15:
    print("벌금 3만원")
elif mycar > speed * 1.15 and mycar <= speed * 1.25:
    print("벌금 5만원")
else:
    print("벌금 7만원")
