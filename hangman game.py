import random
words = ["cloud", "tiger", "chair", "plant", "house"]

clues = {
    "cloud": "Related to internet storage and sky ☁️",
    "tiger": "A wild animal with stripes 🐯",
    "chair": "Used for sitting 🪑",
    "plant": "A living organism that grows in soil 🌱",
    "house": "A place where people live 🏠"
}
word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("Welcome to Hangman Game!")
print("Clue:", clues[word])
print("_ " * len(word))
while incorrect_guesses < max_attempts:
    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print(f"Wrong guess! Attempts left: {max_attempts - incorrect_guesses}")

    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print(display_word)

    if all(letter in guessed_letters for letter in word):
        print("Congratulations! You guessed the word:", word)
        break

if incorrect_guesses == max_attempts:
    print("Game Over! The correct word was:", word)