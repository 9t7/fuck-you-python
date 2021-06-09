import random
countmeter = 0
for customers in range(1,51,1):
    minute = random.randint(5,50)
    if 5<=minute<=15:
        print(f"[O] {customers}번째 손님 (소요시간 : {minute}분)")
        countmeter += 1
    else:
        print(f"[X] {customers}번째 손님 (소요시간 : {minute}분)")
print(f"\n총 탑승 승객 : {countmeter}분")


