def all_times(*times):
    answer = 1
    count = 1
    for it in times:
        if count == 1:
            print("{0}".format(it), end=" ")
            count += 1
        else:
            print("X {0}".format(it), end=" ")
    for do in times:
        answer *= do
    print("= {}".format(answer))
all_times(96,342,3)

#이렇게 for 구문을 두번써서 해도 된다