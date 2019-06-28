
def hangman(word):
    wrong = 0
    man = [
       "___________",#0
       "|     |    ",#1
       "|     O    ",#2
       "|    /|\   ",#3
       "|   / | \  ",#4
       "|    / \   ",#5
       "|  _/   \_ ",#6
       "|__________" #7
   ]
    
    #passes each character of the word into a list 
    rightLetters = list(word) #[ r, h, y, t, h, m]
    board = ["_"] * len(word) #to get the number of underscrores [_, _, _, _, _, _]
    win = False
    print("Hangman!")

   message = "Guess a letter: ")
   letter = input(message)

   if letter in rightLetters: #y
       while letter in rightLetters: # checks if h is in rightLetters
           index = rightLetters.index(letter) # the first index returned in 1
           board[index] = letter
           rletters[index] = "0" # replaces the index of h with 0, so it can break the loop
    else:
        wrong += 1
        print(picture[0: wrong + 2]) #prints up from 0 up to 2
hangman("rhythm")
