surab = {1:"Chocolate", 5:"Milk", 7:7}
print(surab)
print(surab[7])
print(surab[1])
print(surab.get(5))
#할당 되지 않은 키값을 가져올때는 surab[]는 key에러가 나지만
#surab.get()은 None이라 뜬다(에러X, 뒤에 함수 정상적으로 작동)\
#만약 None이 아니라 자신이 설정한 값을 띄우고 싶으면
#surab.get(5,"하고 싶은 말")로 쓰면 된다
#print(surab[2])
print(surab.get(2))
print(surab.get(2,"호로로루ㅜ룰"))
#사전에 키가 있는지 확인하고 싶을때는 
# '키값 in 사전이름'을 사용하면 된다
print(4 in surab) #False
print(1 in surab) #True
#키 이름을 string이나 boolean으로 정할 수도 있다
library = {"하나" : False , "둘" : True}
print(library["하나"])
print(library["둘"])
Shelf = {False : 35, True : 47}
print(Shelf[False])
print(Shelf[True])
#값을 업데이트 하거나 추가할 수 있다
surab[1] = 357
surab[9] = True
print(surab)
#키를 삭제하려면 'del'을 쓰면된다
del surab[1]
del surab[5]
print(surab)
#key들만 출력
print(surab.keys())
#value들만 출력
print(surab.values())
#key,value 둘다 출력
print(surab.items())
#모두다 삭제
surab.clear()
print(surab)