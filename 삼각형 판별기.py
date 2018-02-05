a= int(input("삼각형의 첫 번째 변을 입력하시오"))
b= int(input("삼각형의 두 번째 변을 입력하시오"))
c= int(input("삼각형의 세 번째 변을 입력하시오"))

if a+b <= c or a+c <= b or b+c <= a :
    print('삼각형이 아니다')
elif a==b and b==c :
    print('정삼각형')
elif a==b or a==c or b==c :
    print('이등변 삼각형')
elif a**2 + b**2 == c**2 or a**2 +c**2 == b**2 or b**2 +c**2 == a**2 :
    print('직각 삼각형')
else :
    print('삼각형')
