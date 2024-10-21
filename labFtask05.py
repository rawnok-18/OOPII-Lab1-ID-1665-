"""01"""
class Rectangle():
    def __init__(self, length,width):
        self.length= length
        self.width = width
    def area(self):
        return self.length*self.width
        
    def perimeter(self):
        return 2*(self.length + self.width)
    def display (self):
        print ("length:",self.length)
        print ("width: ",self.width)
r1 =Rectangle(4,5)
r1.display()
print("Area: ",r1.area())
r2 =Rectangle (5,6)
r2.display()
print("Perimeter: ",r2.perimeter())

"""02"""
class Shape():
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name0
        
class Rectangle(Shape):
    def __init__(self, length,width,name):
        super().__init__(name)
        self.length= length
        self.width = width
    def area(self):
        return self.length*self.width
        
    def perimeter(self):
        return 2*(self.length + self.width)
    def display (self):
        print ("Type: ", self.get_name())
        print ("length:",self.length)
        print ("width: ",self.width)
        
r1 =Rectangle(4,5, "Rectangle")
r1.display()
print("Area: ",r1.area())
r2 =Rectangle (5,6)
r2.display()
print("Perimeter: ",r2.perimeter())

"""03"""
class Shape:
    def __init__(self, name):
        self._name = name
        
    def __display_shape_type(self):
        print("Type: ",self._name)
        
    def display_shape(self):
        self.__display_shape_type()
        
class Rectangle (Shape):
    def __init__(self, length, width, name):
        Shape.__init__(self,name)
        self.__length  = length
        self.__width = width
        
    def get_width(self):
        return self.__width
    
    def get_length(self):
        return self.__length
        
    def display(self):
        self.display_shape()
        print("Length: ",self.get_length())
        print("Width: ",self.get_width())
r = Rectangle (4,5, "Rectangle")
r.display()
    
        
