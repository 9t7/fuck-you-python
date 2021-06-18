class magicstore:
    def __init__(self,name,location,price):
        self.name = name
        self.loc = location
        self.p = price
        print("{0}이(가) {1}에 가격[{2}$]로 입고되었습니다^^".format(self.name,self.loc,self.p))
    def sale(self,sale_percent):
        self.p -= self.p*sale_percent/100
        print("{0}{1:>7}% 세일중! 현재가격:{2:>10}$".format(self.name,sale_percent,self.p))



choco = magicstore("초콜릿","D 구역 47번째 전반 오른쪽 중간",419)
print(choco.loc)
milk = magicstore("밀크","A구역 2번째 선반 왼쪽 아래",1.99)
print(milk.p)
milk.new = 123
print(milk.new)
choco.sale(10)