import random

class ImpossibleGame:
    def __init__(self):
        self.moves_left = 7  # Reduced moves for more difficulty
        self.puzzle_stage = 1

    def start_game(self):
        print("Welcome to the Impossible Game!")
        print("Only 1% of players can win. You have 7 moves to complete the game.")
        print("Solve the puzzles, but beware: a single wrong move can end your journey.")
        self.play_game()

    def play_game(self):
        while self.moves_left > 0:
            if self.puzzle_stage == 1:
                if self.puzzle_one():
                    self.puzzle_stage = 2
                else:
                    self.game_over()
                    return
            elif self.puzzle_stage == 2:
                if self.puzzle_two():
                    self.puzzle_stage = 3
                else:
                    self.game_over()
                    return
            elif self.puzzle_stage == 3:
                if self.puzzle_three():
                    self.puzzle_stage = 4
                else:
                    self.game_over()
                    return
            elif self.puzzle_stage == 4:
                if self.puzzle_four():
                    self.win_game()
                    return
                else:
                    self.game_over()
                    return
            else:
                self.game_over()
                return
        print("Out of moves! Game over.")
    
    def puzzle_one(self):
        print("\n--- Puzzle 1: The Number Sequence ---")
        print("Find the number that completes this sequence: 2, 4, 8, 16, ?")
        try:
            answer = int(input("Your answer: "))
            if answer == 32:
                print("Correct! Moving to the next puzzle.")
                self.moves_left -= 1
                return True
            else:
                print("Incorrect! You lose a move.")
                self.moves_left -= 2
                return False
        except ValueError:
            print("Invalid input. You lose a move.")
            self.moves_left -= 2
            return False

    def puzzle_two(self):
        print("\n--- Puzzle 2: The Reverse Word ---")
        word = "python"
        print(f"What is the reverse of '{word}'?")
        answer = input("Your answer: ")
        if answer.lower() == word[::-1]:
            print("Correct! Moving to the next puzzle.")
            self.moves_left -= 1
            return True
        else:
            print("Incorrect! You lose a move.")
            self.moves_left -= 2
            return False

    def puzzle_three(self):
        print("\n--- Puzzle 3: Math Challenge ---")
        print("Solve this math problem: What is the sum of all numbers from 1 to 10?")
        try:
            answer = int(input("Your answer: "))
            if answer == 55:  # 1+2+3...+10 = 55
                print("Correct! Moving to the final puzzle.")
                self.moves_left -= 1
                return True
            else:
                print("Incorrect! You lose a move.")
                self.moves_left -= 2
                return False
        except ValueError:
            print("Invalid input. You lose a move.")
            self.moves_left -= 2
            return False

    def puzzle_four(self):
        print("\n--- Puzzle 4: The Final Door ---")
        print("You are faced with two doors: One leads to victory, the other to defeat.")
        print("Choose wisely!")
        choice = input("Choose door 1 or door 2: ")
        correct_door = random.choice(['1', '2'])  # Randomly decides the winning door
        if choice == correct_door:
            print("You chose the right door!")
            self.moves_left -= 1
            return True
        else:
            print("Wrong door! You lose the game.")
            self.moves_left -= 2
            return False

    def game_over(self):
        print("\nGame Over. Better luck next time!")
    
    def win_game(self):
        print("\nCongratulations! You have won the Impossible Game!")
        print("You are part of the elite 1% who can solve these challenges.")

def play_again():
    while True:
        play = input("\nWould you like to play again? (yes/no): ").lower()
        if play in ('yes', 'y'):
            return True
        elif play in ('no', 'n'):
            return False
        else:
            print("Invalid input. Please answer 'yes' or 'no'.")

# Game loop to allow continuous play
while True:
    game = ImpossibleGame()
    game.start_game()
    
    if not play_again():
        print("Thanks for playing! Goodbye.")
        break
