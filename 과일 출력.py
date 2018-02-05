list1=[]
fruit1 = input('과일을 넣으세요')
list1.append(fruit1)
fruit2 = input('과일을 넣으세요')
list1.append(fruit2)
fruit3 = input('과일을 넣으세요')
list1.append(fruit3)
leng = len(list1)
for i in range(leng-1, -1, -1) :
    print('%s, '%list1[i], end="")
