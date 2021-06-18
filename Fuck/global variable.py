airpods = 141000

def refund(unit):
    airpods = unit*airpods
    print(price)
refund(2)
#함수 내에서 airpods에 값을 대입하려해서
#전역변수 airpods가 아닌 지역변수 airpods가 생성되었다.
#따라서 우리는 전역변수 airpods의 값을 읽어들이려했지만
#지역변수 airpods의 값을 읽어들이게 되어 
#아직 대입된 값이 없어 오류가 나게된다!!!