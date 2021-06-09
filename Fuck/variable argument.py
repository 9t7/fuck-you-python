def all_times(*times):
    answer = 1
    count = 1
    for it in times:
        if count == 1:
            answer = answer*it
            print("{0}".format(it), end=" ")
            count += 1
        else:
            answer = answer*it
            print("X {0}".format(it), end=" ")
    print("= {0}".format(answer))
all_times(24,5,123) #입력 받은 숫자들을 인수로 하려면 어케해야 될까? 고민고민!
