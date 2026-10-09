students = [
    {"name": "Alice", "grades": [5, 4, 5, 3]},
    {"name": "Bob", "grades": [4, 4, 4, 5]},
    {"name": "Charlie", "grades": [5, 5, 5, 5]},
]

student_grade = []
student_name = []

for student in students:
    student_data = student['name'],student['grades']
    student_name.append(student_data[0])
    student_grade.append(student_data[1])

average_grade = {student_name[i] : sum(student_grade[i])/len(student_grade[i]) for i in range(len(student_grade))}
max_grade = []

for key,value in average_grade.items():
    max_grade.append([value,key])

print(max(max_grade)[1],average_grade)
