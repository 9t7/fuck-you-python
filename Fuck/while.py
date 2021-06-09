battery = 100
while battery > 0:
    print("배터리가 {0}% 남았습니다~".format(battery))
    battery -= 1
if battery == 0:
    print("배터리가 없습니다!!!")

'''no = 1
while True:
    print(no)
    no += 1'''

man = '0'
while man != '늙어보이는 신사':
    man = input("누구세요?")
    if man == '늙어보이는 신사':
        print("들어오세요")
    else:
        print("꺼지세요")
