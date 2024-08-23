import hangman_images
import hangman_words
import random

lives = 6 

random_int = random.randint(0,4) 

word = hangman_words.hangman_word[random_int]
print(word)

placeholder = ""

word_length = len(word)

for position in range(word_length):
    placeholder += "_"
print(placeholder)





game_over = False


correct_letters = []



while not game_over:
    
    guess = input("Guess a Letter? \n").lower()



    display = ""


    for letter in word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)
    
    if guess not in word:
        lives -=1
        if lives == 0:
            game_over = True
            print("You Lose")
    
    if "_" not in display:
        game_over = True
        print("You Win")
        
        
    print(hangman_images.stages[lives])