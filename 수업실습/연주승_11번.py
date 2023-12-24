num = int(input("파보나치 수열 몇번쨰 항까지 구할까요?"))
a=1
b=1
for i in range(num):
    print(a,"",end="")
    c = a + b
    a = b
    b = c
