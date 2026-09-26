
import random

WORD_LIST = ["python", "hangman", "internship", "programming", "keyboard"]

MAX_INCORRECT_GUESSES = 6


def choose_word():
    """Randomly select a word from the word list."""
    return random.choice(WORD_LIST)


def display_progress(word, guessed_letters):
    """Show the word with unguessed letters replaced by underscores."""
    display = [letter if letter in guessed_letters else "_" for letter in word]
    return " ".join(display)


def play_hangman():
    word = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0

    print("=" * 50)
    print("Welcome to Hangman!")
    print(f"You have {MAX_INCORRECT_GUESSES} incorrect guesses allowed.")
    print("=" * 50)

    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        print("\nWord: " + display_progress(word, guessed_letters))
        print(f"Incorrect guesses: {incorrect_guesses}/{MAX_INCORRECT_GUESSES}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

        guess = input("Guess a letter: ").lower().strip()

        # Basic input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print("\n" + "=" * 50)
            print(f"Congratulations! You guessed the word: {word.upper()}")
            print("=" * 50)
            return

   
    print("\n" + "=" * 50)
    print("You've run out of guesses! Game over.")
    print(f"The word was: {word.upper()}")
    print("=" * 50)


def main():
    play_again = "y"
    while play_again == "y":
        play_hangman()
        play_again = input("\nPlay again? (y/n): ").lower().strip()
    print("Thanks for playing Hangman!")


if __name__ == "__main__":
    main()
