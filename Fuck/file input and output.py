my_file = open("qwerty.txt","w",encoding = "utf8") #w는 파일을 덮어씌운다 한국어를 쓸 때 utf8로 인코딩을 하지 않으면 오류가 난다
print("oonmyung", file = my_file)
my_file.close()

my_file = open("qwerty.txt","a",encoding="utf8")
my_file.write("gechuk")
my_file.write("deugaza") #자동 줄바꿈 되지 않는다
my_file.close()

my_file = open("qwerty.txt","r",encoding="utf8")
print(my_file.read()) #한번에 모든내용 불러오기
my_file.close()

my_file = open("qwerty.txt","r",encoding="utf8")
print(my_file.readline()) #줄별로 읽기, 한 줄 읽고 커서는 다음줄로 이동
print(my_file.readline()) #print 자동 줄바꿈 있음 없애려면 end = "" 사용
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
print(my_file.readline())
my_file.close()

my_file = open("qwerty.txt","r",encoding="utf8")
read_things = my_file.readlines() #리스트로 읽어와서 출력
for print_things in read_things:
    print(print_things,end="")
my_file.close()

my_file = open("qwerty.txt","r",encoding="utf8")
while True: #반복문을 통한 줄 별 출력 (몇줄인지 모를 때 사용가능)
    readit = my_file.readline() 
    if not readit:
        break
    print(readit)
my_file.close()