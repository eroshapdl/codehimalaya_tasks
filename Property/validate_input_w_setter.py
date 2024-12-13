class Student:
    def __init__ (self, first, last,grade):
        self.first = first
        self.last = last
        self.grade = grade

    def full_name (self):
        name = f"{self.first} {self.last}"
        print (name)
        return name
    
    def last (self):
        return self.last
    
    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade (self, value):
        if value not in range (0,101):
            print ("enter value betn 0 and 100")
            self._grade = None  # set to None to indicate invalid grad
        else:
            self._grade = value  # Only assign if it's a valid grade
        

        self._grade = value

f_name = input ("enter 1st name: ")
l_name = input ("enter last name: ")
grade_n = input ("enter grade: ")
student1 = Student (f_name, l_name, grade_n)
student1.full_name()
print(student1.grade)
    

    


    



        