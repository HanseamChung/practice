def high_score(*para) :
    max1=0
    for i in range(0, int(para)) :
        if int(high_score(i)) >= int(high_score(i+1)) :
            max1 = high_score(i)
        else :
            max1 = high_score(i+1)
    print(max1)

score=input(' 여섯명의 학상의 점수를 입력하시오("/"로 학생을 구분하시오)')
score.split("/")
print(score.split("/"))
print(high_score(score.split("/")))
