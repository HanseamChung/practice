a= int(input("첫번째 양의 정수를 입력하시오"))
b= int(input("두번째 양의 정수를 입력하시오"))
c= int(input("세번째 양의 정수를 입력하시오"))

if (a+b+c)%2 == 0 :
    if a>=b :
        max=a
        if a>=c :
            print(max)
        else :
            max=c
            print(max)
    else :
        max=b
        if b>=c :
            print(max)
        else :
            max=c
            print(max)

else :
    print(a+b+c)
