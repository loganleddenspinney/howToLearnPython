import random
hangman_word = ["sphynx", "quiz", "kazoo", "yuck", "emu" ]

random_int = random.randint(0,4) 

word = hangman_word[random_int]
print(word)
# create an empty string called placeholder 
placeholder = ""
# created word length to find the length of the word
word_length = len(word)
# created for loop to print a "_" for how many letters in the word
for position in range(word_length):
    placeholder += "_"
print(placeholder)


guess = input("Guess a Letter? \n").lower()


# create an empty string called  display
display = ""

# changed the for loop to display the guessed letter if letter was in word else keep _
for letter in word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)
    