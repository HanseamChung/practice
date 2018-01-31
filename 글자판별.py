jumin=input("값을 입력하시오")

if jumin.isalpha() ==True :
    print("글자입니다")
elif jumin.isdigit() ==True :
    print("숫자입니다")
elif jumin.isalnum() ==True :
    print("영숫자 입니다")
else : print("모르겠습니다")


# @@.isdigit( ) : 전체가 숫자로만 구성되어 있는가
#isalpha( ) : 전체가 글자(한글/영어)로만 구성되어 있는가
#isalnum( ) : 전체가 글자와 숫자가 섞여서 구성되어 있는가
#islower( ) : 전체가 소문자로만 구성되어 있는가
#isupper( ) : 전체가 대문자로만 구성되어 있는가
#isspace( ) : 전체가 공백문자로만 구성되어 있는가
