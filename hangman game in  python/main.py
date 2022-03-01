import random

# word_dict = {
#     'python' : "A programming language named after snake",
#     'computer' : "a machine which contains software",
#     'java' : "A programming language named after an island",
#     'mathematics' : "A subject very important for computer",
#     'physics' : "A subject dependent on maths",
#     'chemistry' : "A subject surrounding acids",
#     'rainbow' : "A phenonmenon seen in skies",
#     'science' : "The most important subject for studying",
#     'water' : "Most important compound required for survival for humans"
# }

word_list = [
    'python', 'computer', 'java', 'mathematics', 'physics', 'chemistry', 'rainbow', 'science', 'water'
]

hint_list = ["A programming language named after snake","a machine which contains software","A programming language named after an island","A subject very important for computer","A subject dependent on maths","A subject surrounding acids","A phenonmenon seen in skies","The most important subject for studying","Most important compound required for survival for humans"]

word = random.choice(word_list)
index = word_list.index(word)
hint = hint_list[index]

print("Guess the word! Hint: "+hint)

tries = 12
guesses = ""

while tries != 0:

    failed = 0
    
    for char in word:
        if char in guesses:
            print(char, sep="", end="")
        else:
            print("_", sep="", end="")
            failed += 1

    if failed == 0:
        print("\nYou have won the game")
        break

    print()
    guess = input("Enter an alphabet: ")
    guesses += guess
    if guess not in word:
        tries -= 1
        print("Wrong")
        print("You have ", tries, " chances")

        if tries == 0:
            print("You lose")
