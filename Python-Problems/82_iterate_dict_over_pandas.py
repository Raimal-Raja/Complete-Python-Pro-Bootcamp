import pandas as pd

# student = {"students":['Raimal Raja', "Haroon", "Talha"],
#            'Score':[53,76,84,]}
# new_student = pd.DataFrame(student)
# new_student.to_csv("student.csv")


file = pd.read_csv('student.csv')
for(index, row) in file.iterrows():
    # print(row)
    # print(row.students)
    if row.students == "Raimal Raja":
        print(row.Score)