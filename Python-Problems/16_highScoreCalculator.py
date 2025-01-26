#Method -1 
# student_score = [90, 45, 100, 45, 55]
# highScore = 0
# for score in student_score:
#     if score > highScore:
#         highScore = score
#     else:
#         highScore = highScore

# print(f"The highest score in the class is {highScore}.")


#Method -2
studentScore =  input("Enter a list of student's score: ").split()
for n in range(0, len(studentScore)):
    studentScore[n] = int(studentScore[n])
print(studentScore)
highScore = 0
for score in studentScore:
    if score > highScore:
        highScore = score
    else:
        highScore = highScore
print(f'highest score in the class is {highScore}')