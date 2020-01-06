
# s = "GOLBAL VARIABLE"
#
# def func():
#     mylocal = 10
#     #print(locals())
#     print(globals()['s'])
#
# func()

# def hello(name = "Sabbir"):
#     print("Hello Function Has been run")
#
#     def greet():
#         return "THIS STRING INSIDE GRRET"
#     def welcome():
#         return "THIS STRING INSIDE WELCOME"
#
#     if name == "Sabbir":
#         return greet()
#     else:
#         return welcome()
#
# print(hello("Sabbir"))

def hello():
    return "Hi Sabbir"

def other(func):
    print("HELLO")
    print(func())

other(hello)
