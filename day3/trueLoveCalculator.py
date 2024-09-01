print("The Love Calculator is calculating your score...")
#name1 = input() # What is your name?
#name2 = input() # What is their name?
name1 = "David Beckham"
name2 = "Victoria Beckham"


''' or Love Scores less than 10 or greater than 90, the message should be:

 "Your score is *x*, you go together like coke and mentos."

 For Love Scores between 40 and 50, the message should be:

 "Your score is *y*, you are alright together."

 Otherwise, the message will just be their score. e.g.:

 "Your score is *z*." '''

name1 = name1.lower()
name2 = name2.lower()

t1 = name1.count("t")
r1 = name1.count("r")
u1 = name1.count("u")
ee1 = name1.count("e")
l1 = name1.count("l")
o1 = name1.count("o")
v1 = name1.count("v")
e1 = name1.count("e")
t2 = name2.count("t")
r2 = name2.count("r")
u2 = name2.count("u")
ee2 = name2.count("e")
l2 = name2.count("l")
o2 = name2.count("o")
v2 = name2.count("v")
e2 = name2.count("e")

ts = t1 + t2
rs = r1 + r2
us = u1 + u2
ess = ee1 + ee2
ls = l1 + l2
os = o1 + o2
vs = v1 + v2
es = e1 + e2



trues = ts + rs + us + ess 
loves = ls + os + vs + es
trues = str(trues) 
loves = str(loves)
total = trues + loves
total = int(total)

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total >= 40 and total <=50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}")

'''
combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e
l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))
if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")





'''