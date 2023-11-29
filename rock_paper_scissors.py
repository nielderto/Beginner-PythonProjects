import random
choices = ['rock', 'paper', 'scissors']

while True:
    player = input("Enter(rock, paper, scissors) or enter a number to stop: ").lower()

    if player.isdigit():  
        print("Game stopped. Thanks for playing!")
        break  

    if player not in choices:
        print("Invalid input. Please enter rock, paper, or scissors.")
        continue

    computer = random.choice(choices)
    
    print("Comp: ", computer)

    result = ""

    if player == 'rock' and computer == 'paper':
        result = "Comp wins!"
    
    elif player == 'paper' and computer == 'rock':
        result = "Player wins!"
    
    elif player == 'scissors' and computer == 'rock':
        result = "Comp wins!"

    elif player == 'rock' and computer == 'scissors':
        result = "Player wins!"
    
    elif player == 'paper' and computer == 'scissors':
        result = "Comp wins!"
    
    elif player == 'scissors' and computer == 'paper':
        result = "Player wins!"
    
    elif player == computer:
        result = "It's a tie"
        
    print(result)