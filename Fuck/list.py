number = [1,2,3]
print(number)
room = ["초콜릿","꿀"]
print(room)
#꿀이 몇번째에 있을까?
print(room.index("꿀"))
#사탕를 넣어보자
room.append("사탕")
print(room)
#우유을 세번째에 넣어보자
room.insert(2,"우유")
print(room)
#뒤에서 부터 차례대로 빼보자
print(room.pop())
print(room)
print(room.pop())
print(room)
#초콜릿를 한번 더 넣어주고 초콜릿이 몇개 있는지 세어보자
room.append("초콜릿")
print(room)
print("초콜릿의 개수는?\n%d개!" %room.count("초콜릿"))

#정렬을 해보자!
list = [3,7,5,4,2,6,1]
print(list)
list.sort()
print(list)
#뒤집어보자!
list.reverse()
print(list)
#지워보자!
list.clear()
print(list)
#리스트는 자료형애 구애받지 않는다
mixed_list=[5,"ㅎㄹㅁㄹ",True]
print(mixed_list)
#리스트를 확장 할 수도 있다
one_list = [1,False,"가"]
two_list = ["Ex"]
one_list.extend(two_list)
print(one_list)
#???
First_list = [1,3,2]
Second_list = "Sex"
First_list.extend(Second_list)
print(First_list)
