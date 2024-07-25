# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])


something = 0
for it in student_scores:
   if it > something:
       something = it
       

print(something)
       
    


# "it" is assigned to the list student_scores 
# in the for loop it goes in once and is assigned to the first in the loop 0 