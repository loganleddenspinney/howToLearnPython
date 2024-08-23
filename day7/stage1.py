import random
hangman_word = ["sphynx", "quiz", "kazoo", "yuck", "emu" ]

random_int = random.randint(0,4) 

word = hangman_word[random_int]
print(word)

guess = input("Guess a Letter? \n").lower()


for letter in word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
    
    