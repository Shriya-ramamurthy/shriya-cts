class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

class ReportCard:
    def display(self, student):
        print("Student:", student.name)
        print("Marks:", student.marks)

student = Student("Mokitha", 92)

report = ReportCard()
report.display(student)