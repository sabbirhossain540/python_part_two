#Inheritance
class Animal():
    def __init__(self):
        print("Animal Created!")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")

class Dog(Animal):
    def __init__(self):
        print("Dog Created ")

    def bark(self):
        print("WOOF")

    #Method Overriding
    def eat(self):
        print("Dog Eating")


mya = Dog()
mya.whoAmI()
mya.eat()


#Special Method

class Book():
    def __init__(self,name,authore,pages):
        self.name = name
        self.authore = authore
        self.pages = pages

    #Commonly Use this Method __str__
    def __str__(self):
        return "Title: {} , author: {}, Pages: {}".format(self.name, self.authore, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is Deleted")

b = Book("Python","jose",200)
print(b)
print(len(b))
del b
