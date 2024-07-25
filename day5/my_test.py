student_scores = input().split()
# imput is 98 45 100 60 50

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])


score = 0
for it in student_scores:
    if it > score:
        score = it 
        
print(score)
    
    