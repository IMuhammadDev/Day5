student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

max_is = 0
for it in student_scores:
    if it > max_is:
        max_is = it

print(max_is)
