def calc(v1, op, v2) :
    result = 0
    if op=='+' :
        result=v1 + v2
    elif op =='-' :
        result= v1 - v2
    elif op =='*' :
        result= v1 * v2
    elif op =='/' :
        result= v1 / v2
    elif op =='**' :
        result= v1 ** v2
    return result

res = 0
var1, var2, oper =0, 0, ''

oper = input("계산입력 (+,-,*,/,**) : ")
var1=int(input("첫 번째 숫자 입력 : "))
var2=int(input("두 번째 숫자 입력 : "))




if var2 == 0 and oper == '/' :
    print("0으로 나눌 수는 없습니다")
else :
    res=calc(var1, oper, var2)
    print("##계산기 : %d %s %d = %0.2f" %(var1, oper, var2, res))
