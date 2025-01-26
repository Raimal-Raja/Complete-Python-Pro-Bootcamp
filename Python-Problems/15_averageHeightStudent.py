#Method -1
# students = []
# for student in range( 0, 5):
#     height = int(input("Enter height of students: "))
#     students.append(height)

# print(students)
# sumOfheight = 0
# for height in students:
#     sumOfheight+= height
    
# avgHeight = sumOfheight/len(students)
# print(avgHeight)
    
 
#Method -2   
student_heights = input("Enter a list of student heights ").split()
for n in  range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
sumOfHeight = 0
for height in student_heights:
    sumOfHeight += height
avHeight = sumOfHeight/len(student_heights)
print(sumOfHeight)
print(avHeight)