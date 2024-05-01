import random

words = ["apple", "mango", "orange"]

class Hangman:
    # Initialize the Hangman class
    def __init__(self):
        self.full_word = random.choice(words)
        self.lives = 3
        self.display = ['-' for letter in self.full_word]
        
    # Display the word order
    def show(self):
        return self.display
    
    # Get the word index
    def get_index(self, letter):
        locations = []
        for index, char in enumerate(self.full_word):
            if char == letter:
                locations.append(index)
        return locations
    
    # Update the word after a correct alphabet is guessed
    def update(self, letter):
        indices = self.get_index(letter)
        for index in indices:
            self.display[index] = letter
    
# Game sys
def main():
    game = Hangman()
    while game.lives > 0 and '-' in game.display:
        print("Current word:", ''.join(game.show()))
        user_input = input("Enter a letter: ").lower()
        
        if user_input in game.full_word:
            game.update(user_input)
        else:
            game.lives -= 1
            print(f"Incorrect guess! You have {game.lives} lives left.")
    
    if '-' not in game.display:
        print("Congratulations! You've defused the bomb.")
    else:
        print("Sorry, you've run out of lives. The bomb exploded.")
        

main()

if __name__ == "__main__":
    main()