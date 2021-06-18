def std_weight(height,gender):
    m_height = height*0.01
    if gender == "여자":
        weight = pow(m_height,2)*21
    elif gender == "남자":
        weight = pow(m_height,2)*22
    else:
        print("미지의 성별입니당")
        #조건문 탈출은 없나?
    point_two = round(weight,2)
    print("키{0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height,gender,point_two)) #round를 사용할 수도 있다
    #현재 slice로 값 내림 사용중->round로 반올림
std_weight(151.213,"여자")