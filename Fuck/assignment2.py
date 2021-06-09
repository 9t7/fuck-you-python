leet = list(range(1,21,1))
from random import*
shuffle(leet)
leets = sample(leet,4)
first = leets[0]
second = leets[1:]
print(f'''-- 당첨자 발표 --
치킨 당첨자 : {first}
커피 당첨자 : {second}
-- 축하합니다 --''')

# range(param1, param2, param3)

# param1: 레인지의 시작범위를 지정하는 매개변수 (0일때는 생략가능)

# param2: 레인지의 마지막 범위를 지정하는 매개변수 (지정된 숫자 바로앞까지 레인지를 생성)

# param3: 레인지의 간격을 지정하는 매개변수 (생략하면 기본값 1로 처리)