# 1st input: enter height in meters e.g: 1.65
height = input("1st input: enter height in meters e.g: 1.65\n")
# 2nd input: enter weight in kilograms e.g: 72
weight = input("2nd input: enter weight in kilograms e.g: 72\n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
height = float(height)
weight = int(weight)
BMI = (weight) / (height ** 2)
BMI = round(BMI, 3)
print(BMI)

print(round(3.556,2))

score = 0
gpa = 4.0
isAccepted = True

#fstring
print(f"Your score is {score} your gpa is {gpa} your acceptance is {isAccepted}")
