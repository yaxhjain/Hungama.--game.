import random

# List of predefined words
word_list = ["apple", "zebra", "robot", "india", "grape"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Game variables
guessed_word = ["_"] * word_length
attempts_left = 6
guessed_letters = []

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")

while attempts_left > 0 and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print(f"Attempts left: {attempts_left}")
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❗ Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for i in range(word_length):
            if chosen_word[i] == guess:
                guessed_word[i] = guess
        print("✅ Good guess!")
    else:
        attempts_left -= 1
        print("❌ Wrong guess.")

if "_" not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print("\n💀 Game over! The word was:", chosen_word)