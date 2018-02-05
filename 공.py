
h=float(input('공의 높이를 입력하시오'))
k = 0
while h >= 1/100000 :
    h = h*1/2
    k += 1
    print(h)
    
    
print('공이 튀긴 횟수는 %s 입니다.' %k)
