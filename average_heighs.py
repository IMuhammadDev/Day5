student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
average = 0
for student in student_heights:
    average += student
print(round(average / len(student_heights)))
