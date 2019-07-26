# Chapter 22

# FizzBuzz
# Print numbers 1 to 100. For every number that is divisible by 3 print 'Fizz'.
# For every number that is divisible by 5 print 'Buzz'. If a number is divisible
# by both 3 and 5 print 'FizzBuzz'.
# Example:
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz 

for i in range (1, 101):
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
        continue
    if i % 3 == 0:
        print("Fizz")
        continue
    if i % 5 == 0:
        print("Buzz")
        continue
    print(i)

# Palindrome
# Write a function that takes in a word and determines if it is a # Palindrome.
# Palindrome = a word that is spelled the same way forward and backward.
# Example: racecar spelled backwards is racecar

def isPalindrome:


