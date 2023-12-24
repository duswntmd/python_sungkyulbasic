score=[92,57,75,83,64]
count=1

for i in score:
    if i>=70:
        print(f"{count} 번 학생의 점수는{i} 점 합격입니다.")
    else:
        print(count,"번 학생의 점수는",i, "점 불합격입니다.")
    count +=1
