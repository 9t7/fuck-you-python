#함수 정의는 def로
def fun():
    print("무~야~호~~~"*7)
fun()
def taxifee(money,fee):
    print('''{0}원 받았습니다.\n거스름돈은 {1}원입니다'''\
        .format(money,money-fee)) #줄바꿈 할때는 마지막에 \를 넣는다
    return money-fee, fee
wallet, fee= taxifee(10000,6000) #값 한번에 할당
print("택시비가 {0}원이네,잔액은 {1}원이다".format(fee,wallet))

