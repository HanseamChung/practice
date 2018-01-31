grade1=int(input("1과목 점수를 입력하세요 : "))
grade2=int(input("2과목 점수를 입력하세요 : "))
grade3=int(input("3과목 점수를 입력하세요 : "))

if grade1 < 40 or grade2 < 40 or grade3 < 40 :
    print("과락")
elif (grade1 + grade2 + grade3)/3 >= 60 :
    print("합격")
else :
    print("불합격")
