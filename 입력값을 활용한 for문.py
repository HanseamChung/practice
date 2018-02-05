num = int(input('enter the number : '))
i,fact= 1,1
for i in range(1, num+1) :
    fact= fact*i
    i+=1
print('%d ! = %s' %(num, fact))
