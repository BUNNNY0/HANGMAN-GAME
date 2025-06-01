import random

words = ['apple', 'chair', 'zebra', 'train', 'candy']
word = random.choice(words)
guessed = ['_'] * len(word)
used = set()
tries = 6

print("Welcome to Hangman!\n")

while tries > 0 and '_' in guessed:
    print('Word:', ' '.join(guessed))
    print('Used:', ' '.join(sorted(used)))
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha() or guess in used:
        print("Invalid or repeated guess.\n")
        continue

    used.add(guess)

    if guess in word:
        for i, ch in enumerate(word):
            if ch == guess:
                guessed[i] = guess
        print("Correct!\n")
    else:
        tries -= 1
        print(f"Wrong! {tries} tries left.\n")

if '_' not in guessed:
    print("You won! Word was:", word)
else:
    print("You lost! Word was:", word)