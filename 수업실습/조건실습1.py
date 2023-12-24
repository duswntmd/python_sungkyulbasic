#조건실습1

import turtle as t
t.shape("turtle")

t.penup()
t.goto(100, 100)
t.write("거북이가 여기로 오면 양수입니다.")
t.goto(100, 0)
t.write("거북이가 여기로 오면 0입니다.")
t.goto(100, -100)
t.write("거북이가 여기로 오면 음수입니다.")
t.goto(0, 0)
t.pendown()

s = int(t.textinput("","숫자 입력"))

if s>0:
    t.goto(100, 100)
elif s == 0:
    t.goto(100, 0)
else:
    t.goto(100, -100)
