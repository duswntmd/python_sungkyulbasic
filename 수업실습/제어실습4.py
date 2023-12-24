dan = int(input("몇 단을 출력할까요?"))

for dan in range(2, 10):
    print(dan,"단 출력________")
    for i in range(1, 10):
        print(f"{dan}x{i}={dan*i}") #print(dan,"x",i,"=",dan*i)
