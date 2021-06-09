llolll ="Holy Shit, Sun of beach"
print(llolll.upper())
print(llolll.lower())
print(llolll[0].isupper())
print(len(llolll))
print(llolll.replace("Shit", "Shit fucker"))

where = llolll.index("S")
print(where)
where = llolll.index("S",where + 1)
print(where)
print(llolll.index("Shit")) #문자열이 어디서부터 시작되는지를 반환한다
print(llolll.find("Moon")) #find 함수는 문자열을 찾을 수 없는 경우 -1값을 반환한다
# 그러나 index 함수는 오류가 나면서 종료한다(뒤에 있는 것들은 실행이 안된다)
print(llolll.count("o")) #몇번 나왔는지를 반환한다