import random

# List of predefined words
words = ["python", "computer", "hangman", "program", "coding"]

# Select a random word
word = random.choice(words)

# Variables
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time!")

while incorrect_guesses < max_incorrect:
    # Display the word with guessed letters
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses left:", max_incorrect - incorrect_guesses)

    # Check if word is completely guessed
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    # Get user input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        print("✅ Correct guess!")
    else:
        incorrect_guesses += 1
        print("❌ Wrong guess!")

# If player loses
if incorrect_guesses == max_incorrect:
    print("\n💀 Game Over!")
    print("The word was:", word)