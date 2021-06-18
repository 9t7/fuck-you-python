print("chocolate","milk",sep = " or ",end = " $") 
print("Hello, world!")
#sep = seperate 
#end의 기본값은 줄바꿈이다
price_tag = {"Milk":3.99, "Chocolate":1.59, "AJR CDs":9.99}
for item,dollars in price_tag.items():
    print(item.ljust(10),str(dollars).rjust(7),sep = "|",end = "$\n")

for wait_number in range(1,101,1):
    print("KFC 대기번호",str(wait_number).zfill(3),sep = " -> ")


#사용자 입력을 통해서 값을 받게 되면 항상 문자열로 받게된다
question_mark = input("아무거나 입력하세여~>")
print(type(question_mark))