unique = [1,3,4,6]
mystery = [5,7,10]

for who in range(1,11,1):
    if who in unique:
        continue
    elif who in mystery:
        print(f"{who},오옷!!!!!")
        break
    else:
        print(f"{who},으음으므")

