num=int(input("숫자를 입력하세요."))
if num>10 :
    bs ='큰'
else : bs = '작은'

if num%2 == 0 :
    hole = "짝수"
else : hole = "홀수"
    
print("입력한 숫자 %d 는 10보다 %s %s 입니다." %(num, bs, hole))
