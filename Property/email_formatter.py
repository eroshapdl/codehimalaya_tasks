class Employee:
    def __init__ (self,first,last):
        self.first = first
        self.last = last

    @property
    def email (self):
        email = f"{self.first}.{self.last}@gmail.com"
        return email
        

    @property
    def fullname (self):
        fullname = f"{self.first} {self.last}"
        return fullname
    
    @fullname.setter
    def fullname(self, name):
        first ,last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname (self):
        print ("name deleted")


    
emp_1 = Employee ('Er', 'Pdl')
emp_1.fullname = 'Dp Pdl'
print (emp_1.first)
print (emp_1.email)
print (emp_1.fullname)
del emp_1.fullname


