import random

# List of predefined words
word_list = ["python", "computer", "programming", "developer", "keyboard"]

# Randomly choose a word
secret_word = random.choice(word_list)

guessed_letters = []

wrong_guesses = 0
max_guesses = 6

print("=================================")
print("      WELCOME TO HANGMAN")
print("=================================")

while wrong_guesses < max_guesses:

    display_word = ""

    # Display guessed letters and underscores
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if the player guessed the word
    if "_" not in display_word:
        print("\n Congratulations! You guessed the word:", secret_word)
        break

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct Guess!")
    else:
        wrong_guesses += 1
        print("Wrong Guess!")
        print("Remaining Attempts:", max_guesses - wrong_guesses)

if wrong_guesses == max_guesses:
    print("\n Game Over!")
    print("The correct word was:", secret_word)