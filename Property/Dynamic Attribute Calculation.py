class Rectangle:
    def __init__ (self, length, breadth):
        self.length = length
        self.breadth = breadth
    @property
    def length(self):
        return self._length
    
    @length.setter
    def length (self,value):
        if value <= 0:
            raise ValueError("Length must be positive")
        self._length = value

    @property
    def breadth(self):
        return self._breadth
    
    @breadth.setter
    def breadth (self,value1):
        if value1 <= 0:
            raise ValueError("breadth must be positive")
        self._breadth = value1
    

    @property
    def perimeter(self):
        perimeter_calc = 2 * (self.length + self.breadth)
        print (f"perimeter : {perimeter_calc}")
        
        return perimeter_calc
    
    @property
    def area (self):
        area_calc = self.length * self.breadth
        print (f"area : {area_calc}")
        return area_calc
    
l = int (input ("enter length: "))
b = int (input ("enter breadth: "))
rec_1 = Rectangle (l,b)
rec_1.length
rec_1.breadth
rec_1.perimeter
rec_1.area