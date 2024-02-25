year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap")     
        else:
            print("Not leap")
    else:
        print("Leap") 
else:
    print("Not a Leap")