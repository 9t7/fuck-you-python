for week in range(1,11,1):
    with open("{0}주차 보고서.txt".format(week),"w",encoding="utf8") as week_report:
        week_report.write('''- {0} 주차 주간보고 -\n'''.format(week))
        week_report.write("부서 :\n")
        week_report.write("이름 :\n")
        week_report.write("업무 요약 :")
