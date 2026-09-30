# 🎮 Hangman Game

A simple and interactive **Hangman Game** developed using **Python**. The player has to guess the hidden word one letter at a time before running out of attempts.

## 📌 Project Overview

The Hangman Game is a command-line-based Python project designed to demonstrate fundamental programming concepts such as:

* Variables and data types
* Conditional statements
* Loops
* Strings
* Lists
* Functions
* User input handling
* Random word selection

The game randomly selects a word, and the player attempts to guess it by entering one letter at a time.

## ✨ Features

* 🎲 Random word selection
* 🔤 Letter-by-letter guessing
* ❤️ Limited number of attempts
* ❌ Prevents repeated guesses
* 📊 Displays the current progress of the word
* 🏆 Win/Lose result
* 💻 Simple command-line interface

## 🛠️ Technologies Used

* **Programming Language:** Python
* **Interface:** Command Line / Terminal
* **Libraries:** Python Standard Library

## 🎯 How the Game Works

1. The program randomly selects a word.
2. The selected word is hidden using underscores (`_`).
3. The player enters one letter at a time.
4. If the letter exists in the word, its position is revealed.
5. If the letter is incorrect, the player loses an attempt.
6. Previously guessed letters are tracked to avoid repeated guesses.
7. The player wins by correctly guessing all letters before running out of attempts.
8. The game ends when the word is guessed or all attempts are used.

## 🚀 Getting Started

### Prerequisites

Make sure Python is installed on your system.

Check your Python version:

```bash
python --version
```

### Installation

Clone the repository:

```bash
git clone https://github.com/your-username/hangman-game.git
```

Navigate to the project directory:

```bash
cd hangman-game
```

Run the game:

```bash
python hangman.py
```

## 🎮 Example

```text
Welcome to Hangman!

Word: _ _ _ _ _

Guess a letter: a

Good guess!

Word: _ a _ _ _

Guess a letter: z

Wrong guess!

Attempts remaining: 5
```

## 📂 Project Structure

```text
Hangman-Game/
│
├── hangman.py
└── README.md
```

## 🧠 Concepts Demonstrated

This project demonstrates practical use of:

```text
Python
  │
  ├── Variables
  ├── Strings
  ├── Lists
  ├── Loops
  ├── Conditional Statements
  ├── Functions
  ├── User Input
  └── Random Module
```

## 🔮 Future Improvements

The project can be enhanced by adding:

* Multiple difficulty levels
* Larger word database
* Categories such as Animals, Movies, Countries, etc.
* Score tracking
* Graphical User Interface (GUI)
* Hints
* Multiplayer mode
* Leaderboard

## 👩‍💻 Author
K.Haritha

---

⭐ If you found this project useful, consider giving the repository a star!

