dict = { 
    "Students": [
        ("John", 21, 89),
        ("Jane", 22, 69),
        ("Doe", 30, 80),
        ("Moe", 27, 33),
        ("Lester", 25, 70),
        ("Ng", 55, 75)
    ]
}
Add_Student = ("Mike", 17, 100)
dict["Students"].append(Add_Student)
dict["Students"].remove(("Doe", 30, 80))
print(dict)
high_grade = max(dict["Students"], key=lambda students:students[2])
dict["Students"].sort(key=lambda student:student[2], reverse=True)
print("Student with highest grade:", high_grade)
print(dict)