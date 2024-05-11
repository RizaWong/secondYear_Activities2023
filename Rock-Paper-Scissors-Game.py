from random import choice

game = ["ROCK", "PAPER", "SCISSORS"]

computer_player = choice (game)
score = 0

for i in range (3):
    
    player_input = input("Type your choice between ROCK, PAPER, or SCISSORS (use capital letters only, press 0 to quit): ")     
    
    if player_input == "0":
        print ("Thank you for playing the game.")
        break
    
    elif player_input == "ROCK" and computer_player == "PAPER":
        print ("You lose.")
    
    elif player_input == "ROCK" and computer_player == "SCISSORS":
        score+=1
        print ("You won.") 
    
    elif player_input == "ROCK" and computer_player == "ROCK":
        print ("Draw.")
    
    elif player_input == "PAPER" and computer_player == "SCISSORS":
        print ("You lose.")
    
    elif player_input == "PAPER" and computer_player == "ROCK":
        score+=1
        print ("You won.") 
    
    elif player_input == "PAPER" and computer_player == "PAPER":
        print ("Draw.")
    
    elif player_input == "SCISSORS" and computer_player == "ROCK":
        print ("You lose.")
    
    elif player_input == "SCISSORS" and computer_player == "PAPER":
        score+=1
        print ("You won.") 
    
    elif player_input == "SCISSORS" and computer_player == "SCISSORS":
        print ("Draw.")
    
    elif i == 3:
        print ("GAME OVER.")
    
    else:
        print ("Invalid Input. Please try again.")

    print (f"Score: {score}/3")