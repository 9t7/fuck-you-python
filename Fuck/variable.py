#숫자 형태의 변수와 참 거짓 변수는 문자열에 넣기 위해서
#str이라는 것으로 감싸주어야한다.
#   '+'  기호가 아닌 ','(콤마)로 구분할때는 
# str로 안감싸주어도 된다 
# 대신 콤마로 구분할 경우 무조건 띄어쓰기가 포함된다
name = "초코"
pet = "강아지"
size = "작다"
color = "갈색(초콜릿 색)"
is_it_poodle = size == "작다"
centi = 22.5

print(pet + "이름이 뭐에여?" + name + "에요!")
print("오 ! 매우" + size + " !")
print(color + "이네여")
is_it_poodle = centi < 20
print("푸들인가요?" + str(is_it_poodle))
print("키 몇센치에유?",centi,"에요!")