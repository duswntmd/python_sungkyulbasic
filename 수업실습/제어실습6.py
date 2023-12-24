import random
a=random.randint(1,10)
ans=int(input("1~10까지의 난수를 맞춰보세요"))

while a!=ans:
    if ans<a:
       print("정답은 더 큰수 입니다.")
    else:
       print("정답은 더 작은수 입니다.")
    ans=int(input("다시 입력하세요"))
    
print("정답입니다.")
