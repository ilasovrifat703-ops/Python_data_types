data = [
    {"student": "Alice", "subject": "Math", "grade": 5},
    {"student": "Bob", "subject": "Math", "grade": 4},
    {"student": "Alice", "subject": "History", "grade": 3},
    {"student": "Bob", "subject": "History", "grade": 5},
]

subject_dict = {}

for element in data:
    subject_dict[element['subject']] = {}

for element in data:
    subject_dict[element['subject']][element['student']] = element['grade']

print(subject_dict)
