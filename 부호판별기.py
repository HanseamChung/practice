a=int(input('첫번째 숫자를 입력하시오'))
b=int(input('두번째 숫자를 입력하시오'))

if a ==0 or b ==0 :
    print('0은 입력할 수 없습니다.')
else :
    if (a>0 and b<0) or (a<0 and b>0) :
        print(' 두 수의 곱은 음수입니다.')
    else : print('두 수의 곱은 양수입니다.')
