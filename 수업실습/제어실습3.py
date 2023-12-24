num = int(input("파보나치 수열 몇 번쨰 항까지 구하겠습니까?"))
a=1
b=1
for i in range(num):
    print(a, end="")
    c = a + b
    a = b
    b = c
