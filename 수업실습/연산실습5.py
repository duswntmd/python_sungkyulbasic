#실습5

print("커피 : 2000원, 빵 : 1500원")
coffee = int(input("주문할 커피의 수 입력 : "))
bread = int(input("주문할 빵의 수 입력 : "))
print("="*30)
print(f"주문한 메뉴는 커피 {coffee}잔, 빵{bread}개 입니다.")
print("전체 주문 금액 :", (2000*coffee) + (1500*bread))
