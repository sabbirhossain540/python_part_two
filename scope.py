
# x = 25
#
# def my_func():
#     x = 50
#     return x
#
# print(my_func())

#LOCAL

#Enclosing Function Locals
# name = "This is a global name! "
#
# def greet():
#     name = "Sammy"
#
#     def hello():
#         print("Hello "+ name)
#
#     hello()
#
# greet()



x = 50

def func(x):
    print("x is: ",x)
    x = 1000
    print("local x changed to:",x)

func(x)
