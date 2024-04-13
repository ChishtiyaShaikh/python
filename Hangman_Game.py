import random

def choose_random_word():
    words = ["apple", "banana", "cherry", "orange", "pear", "grape", "watermelon", "pineapple"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    MAX_TRIES = 6
    word_to_guess = choose_random_word()
    guessed_letters = set()
    tries = 0

    print("Welcome to Hangman!")
    while True:
        print(display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in word_to_guess:
            tries += 1
            print(f"Wrong guess! Tries left: {MAX_TRIES - tries}")
            if tries >= MAX_TRIES:
                print("You lost! The word was:", word_to_guess)
                break
        else:
            if "_" not in display_word(word_to_guess, guessed_letters):
                print("Congratulations! You guessed the word:", word_to_guess)
                break

if __name__ == "__main__":
    hangman()
