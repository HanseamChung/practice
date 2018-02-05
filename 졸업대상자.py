esu_s=int(input('이수 학기='))
esu_p=int(input('이수 학점 ='))

if esu_s >= 8 and esu_p >= 140 :
    print('귀하는 정상 졸업자 입니다.')
elif esu_s < 8 and esu_p >= 140 :
    print('귀하는 조기 졸업자 입니다.')
else :
    print('귀하는 졸업 대상자가 아닙니다.')
