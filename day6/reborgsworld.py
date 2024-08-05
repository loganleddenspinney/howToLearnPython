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
    
    
    """
    This is an example on how to use a while in a while with if statements in each while
    
    heres how to do reborgs world hurdle 3 
    https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
   
    def turn_right():
    turn_left()
    turn_left()
    turn_left()
    

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    

while wall_in_front():
    jump()
    if at_goal():
        break
    while front_is_clear():
        move()
        if at_goal():
            break

    
    
    
    
    """
    
    """
    The teacher solved as:
    
    while not at_goal():
        if wall_in_front():
            jump()
        else:
            move()
    
    
    """
    
    
    
    
    """
    
    https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
    rebord hurdle 4
    
    
    def turn_right():
    turn_left()
    turn_left()
    turn_left()
    

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
        
        

while not at_goal():
        if wall_in_front():
            jump()
        else:
            move()
    
    
    
    
    """
    
"""
Reborgs world maze 

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear():
    move()
turn_left()
        
while not at_goal():
    if front_is_clear():
        move()
    elif right_is_clear():
            turn_right() and move()
    else:
        turn_left()







"""