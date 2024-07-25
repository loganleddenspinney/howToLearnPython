import random
rps = input("what do you choose? Type 0 for rock, 1 for papper, or 2 for scissors\n")


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
human = ''''''
cpu_options = [rock, paper, scissors]

if rps == "0":
    human = rock
elif rps == "1":
    human = paper
elif rps == "2":
    human = scissors
else:
    human = "Not Viable"

random = random.randint(0,2)
cpu = cpu_options[random]


if human == rock and cpu == rock:
    print(human)
    print(cpu)
    print("Draw")
elif human == rock and cpu == paper:
    print(human)
    print(cpu)
    print("Paper Beats Rock CPU Wins!")
elif human == rock and cpu == scissors:
    print(human)
    print(cpu)
    print("Rock beats scissors Human Wins!")
elif human == paper and cpu == paper:
    print(human)
    print(cpu)
    print("Draw")
elif human == paper and cpu == scissors:
    print(human)
    print(cpu)
    print("Scissors beats paper CPU Wins!")
elif human == paper and cpu == rock:
    print(human)
    print(cpu)
    print("Paper beats rock Human Wins!")
elif human == scissors and cpu == scissors:
    print(human)
    print(cpu)
    print("Draw")
elif human == scissors and cpu == rock:
    print(human)
    print(cpu)
    print("Rock beats scissors CPU Wins!")
elif human == scissors and cpu == paper:
    print(human)
    print(cpu)
    print("Scissors beats paper Human Wins!")
elif human == "Not Viable":
    print("Not Viable Throw From Human")
    



