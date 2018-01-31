jinsu=int(input("진수(2/8/10/16)를 선택하시오"))
Fn=input("첫 번째 수를 입력하시오")
Sn=input("두 번째 수를 입력하시오")

cal_1= int(int(Fn, jinsu) & int(Sn, jinsu))

print("두 수의 & 연산 결과")
print("16진수 ==>",hex(cal_1))
print(" 8진수 ==>" ,oct(cal_1))
print(" 10진수 ==>" ,cal_1)
print("2진수 ==>",bin(cal_1))

cal_2= int(int(Fn, jinsu) | int(Sn, jinsu))

print("두 수의 | 연산 결과")
print("16진수 ==>",hex(cal_2))
print(" 8진수 ==>" ,oct(cal_2))
print(" 10진수 ==>" ,cal_2)
print("2진수 ==>",bin(cal_2))

cal_3= int(int(Fn, jinsu) ^ int(Sn, jinsu))

print("두 수의 ^ 연산 결과")
print("16진수 ==>",hex(cal_3))
print(" 8진수 ==>" ,oct(cal_3))
print(" 10진수 ==>" ,cal_3)
print("2진수 ==>",bin(cal_3))
