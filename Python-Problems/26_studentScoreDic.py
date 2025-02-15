student_score = {
    "Raimal" : 95,
    "Madhu": 100
}
student_grades = { }
for student in student_score:
    score = student_score[student]
    if score > 90 and score < 96:
        student_grades[student] = "A"
    elif score > 95:
        student_grades[student] = "A+"
    
print(student_grades)
    
 