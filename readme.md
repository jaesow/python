# Python Syntax Cheat Sheet

To write a comment in python use a hashtag at the start of the line: 
  #This is a comment 

To print use the keyword *print*():
  print("Hello World!")

**Important**: Python utilizes proper spacing tp distiguish blocks of code
Python uses a *tab* or *4 spaces* to contain code in a block. The example bleow prints "Hello, WOrld" 100 times.

  for i in range(100):
    print("Hello, world!")

## Data Types
* string -  str ie: "This is a string"
* integer - int ie: "10"
* floating-point-number - float ie: "2.22"
* booleans - bool ie: "True"
* NonType - where None is the value 

In python you dont have to specify the type when making varibale declarations

  x = 100
  
>>100

Here x is assigned to the value of 100.

#### Increment
  x = 10
  x = x +1
  print(x) 
  
>>11

OR

  x = 10
  x +=1
  print(x)
  
>>11

##Arithmatic Operators
**Exponent

% Modulo/remainder

// Integer division/floor quotient 

/Division 

* Multiplication 

-Subtraction

+ Addition

## Comparision Operators 

'>' Greater Than 

'<' Less Than 

'>=' Greater than or equal to 

'<=' Less than or equal to 

'==' Equal 

'!=' Not Equal 

## Logicial Operators 

and
  ie: True and True
  >>True 
or 
  ie: True or False 
  >>False
not
  ie: not True 
  >>False
## Conditional Statements 

Conditional statements can be constructed with keywords: if, elif & else
Fiven x =3. The following consitional statement would yield

x is not 1 or 2 

if x == 1:
  print("x is 1")
elif x == 2:
  print("x is 2")
else:
  print("x is not 1 or 2")

## Functions

Use *def* to define your function and then give your function a name along with parameters to pass in parenthesis 

def functionName(x):
  return x +1
  
functionName(2)
>>3

## Built in Functions

* len() - return the length of the object passed to it
* str() - returns the object that gets passes to it as a string 
* int() - returns the object that get passes to it as an integer 
* float() - retunrs the object that gets passed to it as a float 
* input() - prints the prompt x and returns the users input 

## Required and Optional Parameters 

Python lets you set optional paramets in a function by giving the optional parameters a default value 
  def functionName(x, y = 2):
    return x + y
Here x is required and y is optional. 
  functionName(1, 4)
  >>5
  functionName(1)
  >>3
  
  ## Variable Scope 
  
  **Global Varible** - a varibale with global scope that can be read or written 
  **Local Varibales** - a varible with local scope that can only be read or written 
  
  Use keyword *global* when writing to a global caribale from withon a function 
  
    x = 2
    def f():
      global x
      x += 1
      print(x)
    f()
    >>3
  
  ## Error Handling 

    * SyntaxError: EOL while scanning string literal
    * ZeroDivisionError: division by zero
    * IndentationError: unexpected indent
    
    y = input("Give a value for y:")
    try:
      x = int(y)
     except ValueError:
      print("y must be a number")
    >> Give a value for y:
    >> Python 
    >>y must be a number 
    
   ## Containers
   
   ### Lists 
   * a container that stores objects in a specific order 
   * iterable 
   * mutable 
   
    list = []
    list = list()
    
   use index such as list[1] to find object in the list at a specific index 
   use *append()* to add to a list
   use *pop()* to remove last item from list
   add 2 lists with the addition operator 
   use keyword *in* to check if an item is in a list 
   use keyword *not* paired with *in* to check if an item is not in a list 
   
   ### Tuples 
   * a container thatr stores objects in a specific order
   * immutable 
   * iterable
      tuple = ()
      tuple = tuple()
      
   use index such as tuple[1] to find object in the tuple at a specific index 
   use keywords *in* and *not* just like lists
   
   ### Dictionaries 
   
   * a container that maps a key to a value 
   
    dictionary = {}
    dictionary = dict()
  
  add a value using the following format:
  
    dictionary["key1"] = "value1"
    dictionary["key2"] = "value2"
   
   >>{"key1": "value1", "key2":"value2"}
   
   use keywords *in* and *not* just like lists
   Containers can contain different containers. 
   
   ## Strings 
   
   * strings are immutable
   * use an index to look up characters, indexes start at 0 
   * a **neagative index** can be used to look up items from right to left where [-1] is the last element
   
    string = "Jenaba"
    string[0] = J
    string[2] = n
    
    COME BACK MISSING ITEMS
    
    #### built-in Functions for Strings
    
    **.upper()** - turns string to all upper case chars
    **.lower()** - turns string to all lower case chars 
    **.capitalize()** - capitalizes the first letter of a sentence
    **.format(x)** - will insert into the string to replace the empty {}
    
    
     "Hello, my name is {}".format("Noelle")
     >> "Hello, my name is Noelle"
     
     **.split(x)** - splits a string into a list at each x
      "blue, pink, purple".split(" , ")
      >> ["blue", "pink", "purple"]
      
      **.join()** - used to add new chars between chars of a string; can also be used to turn a list of strin with a new char in between 
      ".".join("python")
      
>> "python"

**.replace(x, y)** - when passed two arguments x and y, will replace x with y 

  string = "Hello World"
  string.replace("l", "!")
  
  >> "He!!o Wor!ld"
  
**.inde** - returns the index of the first occurence of x in a string
  string = "Heloo World"
  string.index('o')
  
>>4

*use he keyword *in* to check if a string contains another string

* escape strings within strings by using the backslash (\")

  "I said \"Hello World""
  
* \n in a string creates a new line 

* use the syntax string [x:y] to slice a string from index x up to index y 

    string = "Hello World"
    string[0:5]

MISSINGS ITEMS

### Modules 
* another name for a puthon file with code in it
* you can import a module using keyword import to use varibales and functions from it 

**Built-in Modules:
* math 
* random
* statistics
*keyword

import math 

math.pow(2,3)

>> 8.0 
**Create your own module by:

* create a python file 
* save the file 
* import the file into another file locates in the same folder 

### Files 

* python had built in functions made to manipulate file objects 
* first step is to open a file using the *open()* function
* the *write()* function lets you write x to a file 
* the *read()* functions lets you read from a file 
* you must clse the file 

### Open file

* the *open* function takes a file and a file mode and return a file object 

* Here are some modes that you can open a file in:
  * "r" - opens a file for readign only
  * "w" - opens a file for writing only; overwrites the fiel if it already exists; if it doesn't exist, creates a new file
  * "w+" - opens a file for readign and writing; overwrites the file if it already exists; if it doesn't exist, creates a new file
  
  st = open("st.text", "w")
  st.write("Hi from Python!") 
  
  
  #### Automatically close file 
  * to automatically close a file without using the *close() function, open your file using a *with-statemnt*
  MISSING 
  
  #### CSV files 
  
  * python has built-in module for working with csv files
  * you can use the *open()* function to open a file and then use the *writer   ?MISSING?
  * use the fucntion *writerow()* to write to the csv object
  
  import csv
  
  with open("st.csv", "w", newline=' ') as f:
  w.writerow(["one", "two", "three"])
  w.writerow(["four", "five", "six"])
  
  >> one, two, three
  >> four, five, six
  
  * the csv module also has a function for reading a csv file: * reader()*
  * the *reader()* function returns an iterable of the rows in the csv file 
  
  import csv
  
  with open("st.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
      print(",".join(row))
  
  >> one, two, three
  
  >> four, five, six 
  
  
  
    



