'''
#2번 문제
n= 1234
sum = 0
while n>0:
    digit=n%10
    sum = sum+digit
    n=n//10
print(sum)
'''
'''
#5번 문제
age = int(input("당신의 나이는?:"))
h = int(input("당신의 키는?:"))

if age >= 10 and h >= 140:
    print("놀이기구 탑승가능")
else:
    print("놀이기구 탑승불가")
'''
'''
#6번 문제
id = 'asdf'
pw = '1234'
input_id = input("아이디 입력: ")
input_pw = input("비밀번호 입력: ")
if id != input_id:
    print("아이디를 찾을 수 없습니다.")
elif pw != input_pw:
    print("패스워드가 일치하지 않습니다.")
else:
    print("환영합니다." )
'''
'''
#7번 문제
add = 0
for i in range(1, 10, 2):
    print(i)
    add += i
print("0부터 10까지 홀수의 합:", add)
'''
'''
#8번 문제
n=int(input("정수를 입력하시오 : "))
fact=1
for i in range(1, n+1):
    fact=fact * i
print(n,"! 은", fact,"이다")
'''
'''
#9번 문제
import turtle as t
t.shape("turtle")
s = int(t.textinput("","맞각형을 그리시겠습니까?(3-6)"))
if s==3:
    t.penup()
    t.goto(0, 100)
    t.pendown()
    t.goto(100, -100)
    t.goto(-100, -100)
    t.goto(0, 100)
elif s == 4:
    t.penup()
    t.goto(100, 100)
    t.pendown()
    t.goto(100, -100)
    t.goto(-100, -100)
    t.goto(-100, 100)
    t.goto(100, 100)
elif s == 5:
    t.penup()
    t.goto(0, 100)
    t.pendown()
    t.goto(100, 20)
    t.goto(70, -100)
    t.goto(-70, -100)
    t.goto(-100, 20)
    t.goto(0, 100)
elif s == 6:
    t.penup()
    t.goto(0, 100)
    t.pendown()
    t.goto(100, 50)
    t.goto(100, -50)
    t.goto(0, -100)
    t.goto(-100, -50)
    t.goto(-100, 50)
    t.goto(0, 100)
else:
    t.goto(0, 0)
'''
'''
#10번 문제
dan = int(input("원하는 단은?"))
for i in range(1, 10):
     print(dan,"x",i,"=",dan*i) #print(f"{dan}x{i}={dan*i}")
'''
'''
#11번 문제
num = int(input("정수 : "))
s = 0
while True:
    s=s+num
    if num == 0:
        break
    num=int(input("정수 : "))
print("합:", s)
'''
'''
#12번 문제
bread=["소금빵","크로아상","스콘"]
drink=["coffee","juice","milk"]
dessert=["cake","choco"]
for b in bread:
    for d in drink:
         print(b,"+",d)
'''
