import random
food = []
a=input("1번째 좋아하는 음식:")
food.append(a)
a=input("2번째 좋아하는 음식:")
food.append(a)
a=input("3번째 좋아하는 음식:")
food.append(a)
a=input("4번째 좋아하는 음식:")
food.append(a)
a=input("5번째 좋아하는 음식:")
food.append(a)
print("내가 좋아하는 음식:", food)
print("오늘 점심:",random.choice(food))
#random.randint(1,100)
#random.randrange(1,101)
