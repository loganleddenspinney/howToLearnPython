stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

                                                                    
                                                            
import random


lives = 6

hangman_word = ["sphynx", "quiz", "kazoo", "yuck", "emu" ]

random_int = random.randint(0,4) 

word = hangman_word[random_int]
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
        
        
    print(stages[lives])