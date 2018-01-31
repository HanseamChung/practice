jinsu=input("16진수를 입력하시오(단 대문자를 사용할 것):")


for i in range(0, len(jinsu)) :
    ch = jinsu[i]
if (49 <= ord(ch) <= 57) or (67<= ord(ch) <=70) :
    print("10진수 ==> %s" % int(jinsu, 16))

else : print("16진수가 아닙니다.")

