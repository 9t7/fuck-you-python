# -------------------중요-------------------
# 함수 정의할때 꼭 넘겨야 하는 인수를 먼저 쓰고, 
# 그 다음에 선택적으로 넘겨야 하는 인수를 써라.
def ads(name,corporation = "경동나비엔", group = "회계"):
    print("회사명:{0}\t부서:{2}\t이름:{1}"\
        .format(corporation, name, group))
ads("김대경")
ads(corporation = "SK하이닉스",name = "김경미", group = "서버구축")