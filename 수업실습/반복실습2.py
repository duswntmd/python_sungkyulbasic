n = int(input("정수 입력:"))

fact = 1
for i in range(1, n+1):
    fact = fact*i #1 2 6 24 120
print(n, "!=", fact)
