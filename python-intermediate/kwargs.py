def create_student_report(name,age,**kwargs):
    student_report={
        "Name":name,
        "Age":age,
        "Subjects":[],
        "Scores":[]
    }

    for subject,scores in kwargs.items():
        student_report["Subjects"].append(subject)
        student_report["Scores"].append(scores)
    return student_report

print(create_student_report('sadichhya',25,physics=100,math=100,python=200))