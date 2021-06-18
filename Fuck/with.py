import pickle
with open("project.pickle","rb") as project_file:
    print(pickle.load(project_file)) #with를 사용하면 따로 파일을 닫을 필요가 없다

with open("with_text.txt","w",encoding="utf8") as filename:
    filename.write("자 드가자 "*11)

with open("with_text.txt","r",encoding="utf8") as filerori:
    print(filerori.read())