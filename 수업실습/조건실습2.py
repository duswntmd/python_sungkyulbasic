#조건실습2

import random

time = random.randint(1, 24)
sunny = random.choice([True, False])

print("지금은", time, "시 입니다.")

if time>=6 and time<9 and sunny == True:
    print("종달새가 노래를 부른다.")
else:
    print("종달새가 노래부르지 않는다.")

if sunny == True:
    print("날씨가 화창합니다.")
else:
    print("날씨가 화창하지 않다.")
