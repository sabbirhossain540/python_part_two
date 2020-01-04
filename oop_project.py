class Calculator():

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2

    def division(self):
        return self.num1 / self.num2

zx = str(input("Please Enter What You want to Do: "))
a = int(input("Please Enter Your First Value: "))
b = int(input("Please Enter Your Second Value: "))

obj = Calculator(a,b)


if(zx == "+"):
    print(obj.addition())
elif(zx == "-"):
    print(obj.subtraction())
elif(zx == "*"):
    print(obj.multiplication())
elif(zx == "/"):
    print(obj.division())
else:
    print("Sorry!! You Enter Nothing")
