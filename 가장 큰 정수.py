a= int(input("첫번째 양의 정수를 입력하시오"))
b= int(input("두번째 양의 정수를 입력하시오"))
c= int(input("세번째 양의 정수를 입력하시오"))

if a<=b<=c or b<=a<=c:
    print(c)
elif a<=c<=b or c<=a<=c:
    print(b)
else :
    print(a)
