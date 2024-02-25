#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator")
bill = float(input("What was the total bill?\n"))
tip = int(input("What percentage tip would you like to give?\n"))
split = int(input("How many people to split the bill?\n"))
price = (bill + (bill * (tip / 100))) / split
price = round(price,2)
price = "{:.2f}".format(price)
print(f"Each person must pay: ${price}")


