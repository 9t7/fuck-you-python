import pickle
project_file = open("project.pickle","wb") #b를 써서 바이너리 명시 #utf8 인코딩을 쓸 수 없다???
project = [123,"사과","시계",True]
print(project)
pickle.dump(project,project_file) #project에 있는 정보를 project_file에 저장
project_file.close()

project_file = open("project.pickle","rb")
project = pickle.load(project_file)
print(project)
project_file.close()