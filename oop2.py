class Circle():
    #Class Object Attributes
    pi = 3.14

    #Method Work as like Constructor
    def __init__(self,radius=1):
        self.radius = radius


    def area(self):
        return self.radius*self.radius* Circle.pi

    def set_redious(self, new_r):
        self.radius = new_r

myc = Circle(3)
myc.set_redious(100)
print(myc.area())
