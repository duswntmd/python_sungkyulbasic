num = int(input("정수 : "))
s = 0
while True:
    s=s+num
    if num == 0:
        break
    num=int(input("정수 : "))
print("합:", s)
