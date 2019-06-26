# chapter 6

#1. print every character in the string "Camus"

string = "Camus"
print( string [0], string [1], string [2], string [3], string [-1] )

#2. Write a program that collects two strings from a user, inserts them into the string "Yesterday I wrote a [response_one]. I sent it to [response_two]!

response_one = input("Enter a word: ")
response_two = input("Enter another word: ")
print("Yesturday I wrote a " + response_one + "." + " I sent it to " + response_two + "!")

#3. Use a method to make the string "aldous Huxley was born in 1894." grammitically correct by capitalizing the first letter in the sentence.

string = "aldous Huxley was born in 1894."
string = string.capitalize()
string = string.replace("h", "H")
print(string)

#4. Take the string "Where now? Who now? When now?" and call a method that returns a list that looks like: ["Where now?", "Who now?", "When now?"].


