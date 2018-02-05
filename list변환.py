word_list = ['scramble','kindly','do','learn']
i = 0
while i <=3 :
    word_list.insert(i, 'un'+ word_list[i])
    del(word_list[i+1])
    i +=1
print(word_list)    
    
