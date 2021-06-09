mise = int(input("현재 미세먼지 농도는??????"))
if 0<mise<40: #and로 0<mise and mise<40 으로 적어도 된다
    print("맑음") 
elif mise == 0:
    print("미쳤다!ㄹㅇ??????????")
elif mise == 40:
    print("보통")
elif mise == 60:
    print("나쁨")
else:
    print("몰라용")   