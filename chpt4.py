# write a function that takes a number as an input and returns that number squared

def squared_func():
    x = input("typer a number:")
    x = int(x)
    x_squared = x **2
    print(x_squared)

squared_func()

#function that accepts a string as a param and prints it

def f(string = "hi"):
    print(string)

f()

#function that takes 3 required params and 2 optional params

x = 3
y = 4
z = 5
def f(x, y, z, a=1, b=2):
    print(x, y, z)

f(x, y, z)




