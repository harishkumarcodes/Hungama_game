import random

# -----------------------------
# Hangman Game - CodeAlpha Task
# -----------------------------

# List of predefined words
words = ["python", "computer", "coding", "developer", "program"]

MAX_WRONG_GUESSES = 6


def play_game():
    secret_word = random.choice(words)
    guessed_letters = []
    display_word = ["_"] * len(secret_word)
    wrong_guesses = 0

    print("\n==============================")
    print("      HANGMAN GAME")
    print("==============================")
    print("Guess the hidden word!")
    print(f"You have {MAX_WRONG_GUESSES} incorrect guesses.\n")

    while wrong_guesses < MAX_WRONG_GUESSES and "_" in display_word:

        print("\nWord :", " ".join(display_word))
        print("Guessed Letters :", " ".join(guessed_letters) if guessed_letters else "None")
        print("Wrong Guesses :", wrong_guesses, "/", MAX_WRONG_GUESSES)

        guess = input("\nEnter a letter: ").lower().strip()

        # Input Validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only ONE alphabet letter.")
            continue

        # Duplicate Check
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Correct Guess
        if guess in secret_word:
            print("Correct!")

            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    display_word[i] = guess

        # Wrong Guess
        else:
            wrong_guesses += 1
            print("Wrong Guess!")

    # Game Result
    if "_" not in display_word:
        print("\nCongratulations!")
        print("You guessed the word:", secret_word)

    else:
        print("\nGame Over!")
        print("The correct word was:", secret_word)


# -----------------------------
# Main Program
# -----------------------------

while True:

    play_game()

    choice = input("\nDo you want to play again? (Y/N): ").lower()

    if choice != "y":
        print("\nThank you for playing!")
        break