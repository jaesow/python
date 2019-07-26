
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
    print(" ".join(board))

    while win == False:
        message = ("Guess a letter: ")
        letter = input(message)

        if letter in rightLetters: #y
            while letter in rightLetters: # checks if h is in rightLetters
                index = rightLetters.index(letter) # the first index returned in 1
                board[index] = letter
                rightLetters[index] = "0" # replaces the index of h with 0, so it can break the loo
            print(" ".join(board))
        else:
            wrong += 1
            print("\n".join(man[0: wrong + 2])) #prints up from 0 up to 2
        if "_" not in board:
            win = True
            print("Congratulations! You win!")
        elif wrong >= 6:
            print("Sorry you lost. The word was {}".format(word))
            break

        
hangman("rhythm")
