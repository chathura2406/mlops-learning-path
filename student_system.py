# 1. Api kalin hadapu Class eka
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = int(marks) # Data enne text widiyata nisa, Marks number ekak karaganna oni (int)

    def get_grade(self):
        # Grade eka return karamu print karanne nathuwa
        if self.marks > 75:
            return "A"
        elif self.marks > 50:
            return "B"
        else:
            return "C"

# --- Main Part (Real World Logic) ---

print("Processing Student Data...\n")

# 2. File eka open karaganna
# 'r' kiyanne Read mode (Kiyawanna witharai)
file = open("students.csv", "r")

# 3. Hama line ekakama kiyawanna (Loop)
for line in file:
    # Line eka: "Kamal,21,85\n"
    
    # strip() -> Line eke agata thiyena spaces ain karanawa
    # split(",") -> "," thiyena than walin kadanawa -> ["Kamal", "21", "85"]
    data = line.strip().split(",")
    
    name = data[0]
    age = data[1]
    marks = data[2]

    # 4. Object eka hadanawa
    student_obj = Student(name, age, marks)
    
    # 5. Result eka gannawa
    grade = student_obj.get_grade()
    
    print(f"{student_obj.name} ge Grade eka: {grade}")

# File eka close krnna  (Memory save karanna)
file.close()