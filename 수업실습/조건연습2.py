#조건연습2

num= int(input("정수 입력:"))

if num % 3 == 0 and num % 5 == 0 :
    print(num, "은 3과 5의 공배수")
else:
    print(num, "은 3과 5의 공배수가 아니다.")
