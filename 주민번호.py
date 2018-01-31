jumin=input("주민등록번호 입력하시오:")

if jumin[-7] =='1' or jumin[-7] =='3' :
    print("남자입니다")
elif jumin[-7] =='2' or jumin[-7] =='4' :
    print("여자입니다")
else : print(jumin[-7])
