students = []
for student in range( 0, 5):
    height = int(input("Enter height of students: "))
    students.append(height)

print(students)
sumOfheight = 0
for height in students:
    sumOfheight+= height
    
avgHeight = sumOfheight/len(students)
print(avgHeight)
    