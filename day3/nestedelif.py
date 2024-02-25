print("Welcome to the rollercoaster")
height = int(input("What is your height in cm?\n"))
age = int(input("What is your age?\n"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Have a free ticket!")
    else:
        bill = 12
        print("Adult tickets are $12.")
        
    wantsPhoto= input("Do you want a photo taken? Y or N. ")
    if wantsPhoto == "Y":
        bill +=3
    print(f"Your bill is ${bill} ")
        
        
        
else:
    print("You cannot ride the rollercoaster.")
    