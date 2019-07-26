# 1. Create RECTANGLE and SQUARE classes with a method called calculate_perimeter
# that calculates the perimeter of the shapes they represent. Create RECTANGLE
# and SQUARE objects and call the mthod on both of them.

class Rectangle:
   def __init__(self, l, w):
       self.length = l
       self.width = w

   def calculate_perimeter(self):
       return (self.length * 2) + (self.width * 2)


#class Square:
   #def __init__(self, s):
      # self.side = s

   #def calculate_perimeter(self):
       #return (self.side * 4)

rectangle1 = Rectangle(9, 3)

#square1 = Square(5)

print(rectangle1.calculate_perimeter())
#print(square1.calculate_perimeter())

#2. Define a method in your SQUARE class called change_size that allows you to
# pass in a number that increases or decreases(if the number is negative) each
# side of a SQUARE object by that number.

class Square:
    def __init__(self, s):
       self.side = s
    def change_size(self, number):
        self.side = self.side + number
        return self.side
         
    def calculate_perimeter(self):
       return (self.side * 4)

square1 = Square(20)
new_square = square1.change_size(3)
print(new_square)

#3. Create a class called SHAPE. Define a method in it called what_am_i that
# prints "I am a shape" when called. Change your SQUARE and RECTANGLE classes
# from the previous challenges to inherit from SHAPE, create SQUARE and RECTANGLE
# objects, and call the new method on both of them.


class Shape:
   def __init__(self):
   def what_am_i(self):
      print("I am a shape")
square_shape = Square(7)
rectangle_shape = Rectangle(10,21)

square_shape.what_am_i()
rectanle_shape.what_am_i()

# 4. Create a class called HORSE and a class called RIDER. Use composition
# to model a horse that has a rider.

class HORSE:
   def __init__(self, rider):
      self.rider = rider

class RIDER:
   def __init__(self, name):
      self.name = name

megan = Rider("Megan thee Stallion")
texas = Horse(megan)

print(texas.rider.name)


#CHAPTER 14
#1

#2 Change square class so that when u print a square object, a message prints, telling u the length of each of the 4 sides of the shape


class Square:
    def __init__(self, s):
       self.side = s
    def change_size(self, number):
        self.side = self.side + number
        return self.side
         
    def calculate_perimeter(self):
       return (self.side * 4)

    def __repr__(self):
       return (self.side + "by")*3 + self.side



print(sqaure1)

#3 Write a function that takes in 2 objects as paramets and returns true if they are the same object and false if not

def compareShape(object1, object2):
   print(object1 is object2) #is does the comparison 


