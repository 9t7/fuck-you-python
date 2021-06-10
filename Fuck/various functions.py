print(abs(-34)) #절대값 함수
print(pow(3,2)) #제곱 함수
print(max(3,2,4)) #최댓값 함수
print(min(3,2,4)) #최솟값 함수
print(round(3.1415926)) #반올림 함수
import random
from math import *
print(floor(2.99)) #내림
print(ceil(2.09)) #올림
print(sqrt(0.49)) #제곱근

print(random.random()) #0이상 1미만의 실수를 반환한다
print(random.random()*10000) #0이상 10000미만의 실수 출력
print(int(random.random()*10)) #0이상 10미만의 정수값 출력

print(int(random.random()*45+1))
print(int(random.random()*45+1))
print(int(random.random()*45+1))
print(int(random.random()*45+1))
print(int(random.random()*45+1))
print(int(random.random()*45+1))

print(random.randrange(1,46)) #1이상 46미만
print(random.randint(1,45)) #1이상 45이하
print("날짜는 " +str(random.randint(3,28)))
print("정수" + str(5))