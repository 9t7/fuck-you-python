Mcdonalds = [1,2,3,4,5,6,7]
print(Mcdonalds)
Mcdonalds = [i + 800 for i in Mcdonalds]
print(Mcdonalds)

#문자열을 길이로 변환
letter = ["바나나","딸기","수박"]
letter = [len(i) for i in letter]
print(letter)

#문자를 대문자로 변환
fixer_upper = ["So he's a bit of a fixer-upper"]
fixer_upper = [i.upper() for i in fixer_upper]
print(fixer_upper)