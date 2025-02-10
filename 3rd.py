students = (
    ("Toma", 20, 88),
    ("Tonmoy", 22, 75),
    ("monalisa", 19, 92),
    ("Joy", 21, 85),
    ("Eva", 20, 78)
)
sorted_students = sorted(students, key=lambda student: student[2])
for student in sorted_students:
    print(student)
