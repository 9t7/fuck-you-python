#집합-중복안됨 순서없음
ok_set = {1,1,2,2,2,3,3,3,3}
print(ok_set)

cake = {"Michael","Alice"}
sweet = set(["Michael","Jimmy","Joe","Andre"]) #이렇게도 세트를 설정할 수 있다

print(cake)
print(sweet)

#add 값 추가
cake.add("Hana")
print(cake)

#remove 값 제거
sweet.remove("Jimmy")
print(sweet)

# 교집합
print(cake & sweet)
print(cake.intersection(sweet))

#합집합
print(cake | sweet)
print(sweet.union(cake))

#차집합
print(cake - sweet)
print(cake.difference(sweet))