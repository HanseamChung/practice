grade=int(input("점수를 입력하세요 : "))

if grade >= 95 and grade <= 100 :
    print("a+")
elif grade >= 90 and grade < 95 :
    print("a")
elif grade >= 85 and grade < 90 :
    print("b+")
elif grade >= 80 and grade < 85 :
    print("b")
elif grade >= 75 and grade < 80 :
    print("c+")
elif grade >= 70 and grade < 75 :
    print("c")
elif grade >= 65 and grade < 70 :
    print("d+")
elif grade >= 60 and grade < 65 :
    print("d")
else :
    print("f")
