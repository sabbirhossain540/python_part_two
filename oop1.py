class Dog():
    #CLASS OBJECT ATTRIBUTE
    species = "mammal"
    #INIT IS AS LIKE CONSTRACTOR
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name


mydog = Dog("Lab","Sammy")
print(mydog.breed)
print(mydog.name)
print(mydog.species)
