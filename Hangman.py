from words import words
import random

word = random.choice(words)  # Word that user will be guessing
visible_word = ""  # Represents the "Fill-in-the-blanks" area from Hangman
incorrect_letters = []
body_parts = 9  # Fail condition

# Fill 'visible_word' with 'len(word)' of "blanks" (underscores)
for i in range(len(word)):
    visible_word = visible_word + "_"

# Guess letters as long as user haven't guessed the full word or failed over 'body_parts' times
while len(incorrect_letters) < body_parts and visible_word != word:
    letter_found = False

    # Print "Fill-in-the-blanks" area and incorrectly guessed letters
    print(visible_word)
    print(*incorrect_letters, sep="\u0336, ", end="\u0336")
    print()

    guess = input("Enter letter: ").lower()

    # Error check.
    if len(guess) > 1 or guess.isspace() or guess == "":
        print("Please enter a single letter.")
    elif guess in incorrect_letters or guess in visible_word:
        print(f"You have already guessed '{guess}'.")
    else:
        # Check if the user's guessed letter is in the word
        for i in range(len(word)):
            if word[i] == guess:
                visible_word = visible_word[:i] + guess + visible_word[i + 1:]
                letter_found = True

        if not letter_found:
            print(f"The word does not contain a '{guess}'")
            incorrect_letters.append(guess)

# Check if user actually won or are just really bad at guessing words
if len(incorrect_letters) == body_parts:
    print("\nHangman!")
    print(f"The word was \"{word}.\"")
else:
    print(f"\nCongrats! You guessed the word '{word}' with {len(incorrect_letters)} misses!")
