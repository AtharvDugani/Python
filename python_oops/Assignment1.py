from datetime import datetime
from grade import grades
import time
import threading

class student:
    def __init__(self,  name, rollno):
        self.rollno = rollno
        self.name = name
        self.__marks = 0
        self.admission_date = None


    def set_marks (self, marks):
        try:
            if marks > 100 or marks < 0:
                raise Exception("Invalid Marks")
        except Exception as e:
            print(e)
        else:
            self.__marks = marks
            
    def get_marks(self):
        return self.__marks


    def set_admission_date(self, date):
        self.admission_date = datetime.strptime(date, "%d-%m-%Y")

    def report_generation(self):
        print("Student Report as Follows: ")
        print(self.rollno, self.name, self.get_marks())
        grades(self.get_marks())
        time.sleep(4)
        print("Good Luck!!")
        
    def display(self):
        print(self.rollno, self.name)
        if self.admission_date is not None:
            print(self.admission_date.strftime("%d-%m-%Y"))
        else:
            print("Admission Date: Not set")

# MeritStudent is class which is inherited from Student class
class MeritStudent(student):
    def grade(self):
        marks = self.get_marks()
        if marks >= 85 and marks <=100:
            print("Merit A")
        elif marks >= 80 and marks <90:
            print("Merit B")
        else: 
            print("Merit C")
    
# Department is the class with list of students in that department 
class department:# class
    def __init__(self,deptname):
        self.deptname = deptname
        self.students = [] # list of students i.e container

    def add_student(self,s):
        self.students.append(s)
        
    def display_student(self):
        for s in self.students:
            print(s.rollno, s.name)

s1 = student("Atharv", 101)
s1.display()
print(s1.get_marks())
print()

s1.set_marks(98)
s1.set_admission_date("23-08-2026")
s1.display()
print(s1.get_marks())
grades(s1.get_marks())
print()

s5 = MeritStudent("Tanaya",105)
s5.set_marks(90)
s5.display()
s5.grade()


s2 = student("Vansh", 101)
s3 = student("Sonal", 102)
s4 = student("Sanjana", 103)

thread1 = threading.Thread(target=s1.report_generation())
thread2 = threading.Thread(target=s2.report_generation())

thread1.start()
thread2.start()
thread1.join()
thread2.join()



d1 = department("MCA")

d1.add_student(s1)
d1.add_student(s2)
d1.add_student(s3)
d1.add_student(s4)
print(f"\nStudents in {d1.deptname} Department")
d1.display_student()