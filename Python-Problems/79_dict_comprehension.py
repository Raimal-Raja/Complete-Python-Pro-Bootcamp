import random
names = ["Raimal Raja", "Haroon", "faizan", "talha"]

student_score = {student:random.randint(1,100) for student in names}
# print(student_score)

pass_student = {student:score for (student, score) in student_score.items() if score >= 60}
print(pass_student)