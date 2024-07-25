student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
totalheight = 0
for height in student_heights:
    totalheight += height
    
how_many = n+1

print(f"Total height is: {totalheight}")
print(f"Number of kids is: {how_many}")
print(f"The average height is {round(totalheight/how_many)}")


'''print(int(totalheight/how_many))
'''