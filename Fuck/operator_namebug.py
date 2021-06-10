print(3**5) #3의 5제곱
print(10%5) #10을 5로 나눴을때의 나머지
print(78%4)
print(47//3) #47을 3으로 나눴을때의 몫
print(5); print(6)
print(5<=5) #비교 연산자 -> true
print(3>=8) #False
print(9==9) #True
print(3==4) #False
print(5//2==2) #True
print(6 + 17 ==22) #False
print(1 != 132) # '!='은 앞뒤가 같지 않다는 의미이다
print(not(1 != 132)) #False
'''not은 뒤의 결과의
반대를 나타낸다'''
print((3==3) and (3<19)) #True
print((3==3) & (3<19)) #True
# 'and' 와 '&'는 같은 의미이다
print((4%2==0) & (3//2==2)) #False
'''만약 앞 항이나 뒷 항 둘중하나라도
False 이면 결과가 False로 나타난다'''
print((5==7) or (not(5==7)))
# 'or'은 앞항이나 뒷항 둘중하나라도 True
# 이면 True로 표시된다
print(not((5==7) or (5==7)))
print((4 >= 7) | (7**2==40))
# 'or'을 '|'로 쓸 수도 있다
print(3<5<=5) #True
print(2>5>3) #False
print(3<5>3) #True
print(1<4>3<23) #True
