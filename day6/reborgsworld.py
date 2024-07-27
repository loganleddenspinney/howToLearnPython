def turn_right():
    turn_left()
    turn_left()
    turn_left()
    

def morg():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for i in range(6):
    morg()
    
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# while loop (this while does the same as the for loop above)

number_of_hurdles = 6

while number_of_hurdles > 0:
    morg()
    number_of_hurdles -= 1
    
# for 
#for item in list_of_items:
#   do something to each item
#
#for number in range(a,b):
#   print(number)

#while
#
#while something_is_true:
#   do somthing repeatedly

# while not at_goal():
#    morg()
    