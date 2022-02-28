import random


guess_list = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board']

guesses = ""

name = input("What is your name? ")
print("Good Luck "+name)

tries = 12

word = random.choice(guess_list)

print("The word has ", len(word), " alphabets")
print("Guess the Characters")
while tries != 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_", end="")
            failed += 1
        
    if failed == 0:
        print("\nYou have won the game")
        break
    print()
    guess = input("Enter an alphabet: ")
    guesses += guess

    if guess not in word:
        tries -= 1
        print("\nWrong")
        print("You have ", tries, " more chances")
        if tries == 0:
            print("You lose")