# **Impossible Game**
![222222](logo.svg)

> **Only 1% of players can win this game!**

This is a terminal-based puzzle game written in pure Python, designed to be extremely challenging. The game tests your logic, memory, and attention to detail with a series of difficult puzzles. One wrong move, and you lose valuable chances to win.

The game is designed to be **highly difficult**, where even slight mistakes can end your journey. It features:
- **Beautiful colorful interface** using the `rich` library.
- **An ASCII banner** created with the `pyfiglet` library for a stylish welcome screen.
- A combination of puzzles involving numbers, word reversals, math problems, and luck!

## **Table of Contents**
- [Features](#features)
- [How to Play](#how-to-play)
- [Installation](#installation)
- [Game Mechanics](#game-mechanics)
  - [Puzzle 1: The Number Sequence](#puzzle-1-the-number-sequence)
  - [Puzzle 2: Reverse the Word](#puzzle-2-reverse-the-word)
  - [Puzzle 3: Math Challenge](#puzzle-3-math-challenge)
  - [Puzzle 4: The Final Door](#puzzle-4-the-final-door)
- [Technologies Used](#technologies-used)
- [Future Enhancements](#future-enhancements)

## **Features**
- **Beautiful User Interface**: The game uses the `rich` library to make the text colorful and interactive.
- **ASCII Art Title**: Using `pyfiglet`, the game starts with a stylish ASCII banner.
- **Highly Challenging**: Each puzzle requires thought and attention, and mistakes are heavily penalized.
- **Limited Moves**: You only have **7 moves** to complete the entire game.
- **Replay Option**: After each game, the player can choose to play again.
- **Puzzle Variety**: The game includes math challenges, word puzzles, and even luck-based choices.

## **How to Play**
1. **Start the game**: The game will start with an ASCII banner and a colorful introduction.
2. **Solve the puzzles**: The game will present you with a series of puzzles.
   - For each puzzle, you must input your answer. Wrong answers cost more moves, so think carefully!
3. **Limited Moves**: You only have 7 moves. Every wrong answer reduces your moves significantly, making it harder to win.
4. **Complete all 4 puzzles**: If you solve all the puzzles correctly within the move limit, you win the game!

Each puzzle increases in difficulty, and the final one even introduces an element of luck, where you must choose the correct door to win.

## **Installation**

### Step 1: Clone the repository or download the source code.
```bash
git clone https://github.com/rkstudio585/ImpossibleGame.git
cd ImpossibleGame
```

### Step 2: Install required dependencies.
You will need to install `rich` and `pyfiglet` to run the game.
```bash
pip install rich
pip install pyfiglet
```

### Step 3: Run the game.
```bash
python impossible_game.py
```

## **Game Mechanics**

### **Puzzle 1: The Number Sequence**
- The first puzzle is a number sequence: `2, 4, 8, 16, ?`
- The player must recognize the pattern (each number doubles).
- **Correct Answer**: 32
- **Wrong answer penalty**: Lose 2 moves.

### **Puzzle 2: Reverse the Word**
- The second puzzle asks the player to reverse a word: `python`.
- The correct answer should reverse the word and match: `nohtyp`.
- **Wrong answer penalty**: Lose 2 moves.

### **Puzzle 3: Math Challenge**
- The third puzzle is a math problem: "What is the sum of all numbers from 1 to 10?"
- **Correct Answer**: 55 (sum of integers from 1 to 10).
- **Wrong answer penalty**: Lose 2 moves.

### **Puzzle 4: The Final Door**
- The final puzzle is based on chance. The player has to choose between **door 1** or **door 2**.
- One door leads to victory, and the other leads to defeat. The correct door is randomly chosen at runtime.
- **Correct Answer**: Randomly assigned at runtime.
- **Wrong answer penalty**: Lose 2 moves.

## **Technologies Used**
- **Python**: The core programming language used for the game.
- **`rich`**: For colorful and rich text formatting in the terminal.
- **`pyfiglet`**: For generating ASCII art for the game banner.
- **`random`**: For randomizing choices in the final puzzle.

## **Future Enhancements**
This game can be expanded with additional features such as:
- **More Puzzles**: Introduce more types of logic and pattern-based puzzles to further challenge the player.
- **Multiple Difficulty Levels**: Offer easy, medium, and hard difficulty settings.
- **Save Progress**: Allow players to save and load their game progress.

---
