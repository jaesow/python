# Print 3 differnt strings
print("Hi my name is Jenaba!")
print("I am a rising junior at Howard University.")
print("I am a computer science major")

# Print a message if a var is less than 10, and a diff message if a var is greater than or equal to 10
var = 8
if var < 10:
    print("The variable is less than 10!")
else:
    print("The varible is less than or equal to 10!")
    
# Print message if the var is less than or equal to 10, diff message if var is greater than 10 but less than or equal to 25, and another message if the var is greater than 25

var = 15
if var <= 10:
    print("The varibale is less than or equal to 10!")
elif var <= 25:
    print("The varible is greater than 10, but less than or equal to 25!")
else:
    print("The variable is greater than 25!")

# divide 2 vars and print their remainder

var1 = 10
var2 = 5
remainder = var1 % var2
print(remainder)
