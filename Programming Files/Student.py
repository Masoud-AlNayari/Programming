class Student:
    def __init__(self, name, college, gpa, courses): 
        self.name = name
        self.college = college
        self.courses = courses
        self.gpa = gpa

    def myfunc(anything):
        print("Student's name is " + anything.name)
        
    def printCourses(self):
        print("The student is registered in the following courses:\n 1. " + self.courses[0]
              + "\n 2. " + self.courses[1])

p1 = Student("Bob", "Engineering", "3.2", ["Math","Computer Science"])
p1.myfunc()
p1.printCourses()
