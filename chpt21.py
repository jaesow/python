#1. Reverse a string using a stack

string1 = "I love sour patches"
list1 = list(string1)
list2 = []

while len(list1) > 0:
    item = list1.pop()
    list2.append(item)

print(list2)


#2 Use a stack to create a new list with the items in the folllowing list revered: [1. 2, 3, 4, 5]

numbers = [1, 2, 3, 4, 5]

newNumbers = [ ]

while len(numbers) > 0:
    popped = numbers.pop()
    newNumbers.append(popped)

print(newNumbers)


# Anagram
# Write a function that takes in two words and determines if the words are an
# anagram of each other.
# Anagram = A word created by rearranging the letters of another word.
# Example: iceman and cinema
string2 = "cinema"
string1 = "iceman"
word1 = list(string1)
word2 = list(string2)
def isAnagram(word1, word2):
    # alphabatize each word and then see if the outputs are equal to eachother
    word1.sort()
    word2.sort()
    print(word1, word2)
    if word2 == word1:
        print("Anagram") 
isAnagram(word1, word2)



