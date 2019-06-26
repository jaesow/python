# write a function that takes a number as an input and returns that number squared


def squared_func():
    """
    Prints x squared
    
    """
    x = input("type a number:")
    x = int(x)
    x_squared = x **2
    print(x_squared)

squared_func()

#function that accepts a string as a param and prints it


def f(string = "hi"):
     """
    Prints string
    :param string: str. 
    :return: str input
    
    """
    print(string)

f()

#function that takes 3 required params and 2 optional params

x = 3
y = 4
z = 5
def f(x, y, z, a=1, b=2):
     """
    Prints x y and z
    :param: x: int.
    :param: y: int.
    :param: z: int.
    
    """
    print(x, y, z)

f(x, y, z)

# two functions. First: takes an integer as a param, return int/2. Second: takes an int as param, returns int*4. Call first func, save result as var that is passed into second func as param

x= input ("enter a number: ")
x = int(x)
def first(x):
    """
    Returns result 
    """
    result = x/2
    print(result)
    return result

def second(y):
    result3 = y*4
    print(result3)
    
result2 = first(x)
second(result2)

#func that converts a string to a float, returns result, use exception handling to catch exception


try:
    x = input ("type a number: ")
    x = float(x)
    print(x)
except ValueError:
        print("Invalid entry. Type a number")

#add a docstring to all of the function you wrote in challeneges 1-5


    





