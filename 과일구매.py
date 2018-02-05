fruits = {'사과' : 1000, '포도' : 3000, '배' : 2000, '귤' : 500} 
f1_n=input("구입하려는 과일의 이름을 입력하세요(입력을 종료하시려면 q를 입력하세요)")



if f1_n == 'q' :
    print('입력을 중지합니다')
elif f1_n=='사과'or' 포도'or'귤'or'배' :
    f1_q=int(input("구입하려는 과일의 갯수를 입력하세요"))
    f2_n=input("구입하려는 과일의 이름을 입력하세요(입력을 종료하시려면 q를 입력하세요)")
    if f2_n =='q' :
        print('귀하는 %s -> %n : 금액 %n' %(f1_n, f1_q, int(fruits[f1_n]) ) )
    elif f2_n == '사과'or' 포도'or'귤'or'배' :
        f2_q=int(input("구입하려는 과일의 갯수를 입력하세요"))
        total = int(int(fruits[f1_n]) * f1_q + int(fruits[f2_n]) * f2_q)
        f1_mm = int(f1_q//10)
        f2_mm = int(f2_q//10)
        if f1_n=='포도' and f1_q >= 3 :
             total = 0.9 * total
        elif f2_n=='포도' and f2_q >= 3 :
             total =  0.9*total
        elif f1_n=='귤' and f1_q//10 >= 1 :
             f1_q = f1_q- 2*f1_mm
        elif f2_n=='귤' and f2_q//10 >= 1 :
             f2_q = f2_q- 2*f2_mm     
                
        print('귀하는 %s -> %d : 금액 %d %s -> %d : 금액 %d 총 금액 %d을 구입했습니다.' %(f1_n, f1_q, int(fruits[f1_n]),f2_n, f2_q, int(fruits[f2_n]), total) )
else : print('과일이름을 입력하시오')
