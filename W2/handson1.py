#students grade management
students = []
def add_student(name,grade):
    students.append ({"name":name, "grade":grade})

def calculate_average():
    total=sum(std['grade'] for std in students)
    return total/len(students) if students else 0

add_student("Debapriya",99)
add_student("Neha",98)
add_student("Tripan",99)
add_student("Suvendu",85)
print(students)
print(f"Average grade: {calculate_average():.2f}")



