#실습4

money = int(input("투입한 돈: "))
price= int(input("물건 값: "))
chang = money-price
print("거스름돈: ", money - price)
print("500원 동전의 개수: ", chang//500 )
print("100원 동전의 개수: ", (chang%500)//100 )
