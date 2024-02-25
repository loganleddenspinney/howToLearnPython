# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = weight / (height ** 2) 

if BMI < 18.5:
  print(f"You are under weight your bmi is {BMI}")
elif BMI < 25:
  print(f"You are a normal weight your bmi is {BMI}")
elif BMI < 30:
  print(f"You are slightly overweight your bmi is {BMI}")
elif BMI < 35:
  print(f"You are obese your bmi is {BMI}")
else:
  print(f"You are clinically obese your bmi is {BMI}")