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
# Conditional Statements 

Conditional statements can be constructed with keywords: if, elif & else
Fiven x =3. The following consitional statement would yield

x is not 1 or 2 

if x == 1:
  print("x is 1")
elif x == 2:
  print("x is 2")
else:
  print("x is not 1 or 2")
  
## Error Handling 

* SyntaxError: EOL while scanning string literal
* ZeroDivisionError: division by zero
* IndentationError: unexpected indent


