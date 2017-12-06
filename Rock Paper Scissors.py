import random

# Launchcode Project
rock = 1
paper = 2
scissors = 3

humanScore = 0
compScore = 0
numOfGames = int(input("How many games should be played in a 'best of' format?"))
winningScore = int((numOfGames/2) + .5)

#   get the human's input, the computer's choice and ddetermine winner of current round 

while humanScore != winningScore and compScore != winningScore:
    humanChoice = int(input("what is your choice? 1 = rock, 2 = paper. 3 = scissors"))
    compChoice = random.randint(1,3)
    if humanChoice == compChoice:
        print("We both picked the same instrument - ties don't count")
    elif humanChoice == 1 and compChoice == 3:  
        
        print("You win!  The computer picked scissors")
        humanScore = humanScore + 1
        print("Your score is now", humanScore, "and the computer's score is", compScore)
    elif humanChoice == 2 and compChoice == 1:
         
         print("You win!  The computer picked rock")
         humanScore = humanScore + 1
         print("Your score is now", humanScore, "and the computer's score is", compScore)
    elif humanChoice == 3 and compChoice == 2:
         
         print("You win!  The computer picked paper")
         humanScore = humanScore + 1
         print("Your score is now", humanScore, "and the computer's score is", compScore)
    else:
        print("You lose!  The computer picked", compChoice)   
        compScore =compScore + 1
        print("Your score is now", humanScore, "and the computer's score is", compScore)
    
     
    
    
 # determine who won the overall game   

if humanScore > compScore:
    print("Congratulations! You won.  Your score is:", humanScore, "and the computer's score is", compScore)                  
else:
    print("You lost! Better luck next time Your score is:" , humanScore, "and the computer's score is", compScore)                           

