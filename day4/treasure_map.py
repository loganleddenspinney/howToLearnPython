line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?

horizontal = position[0].lower()
vertical = int(position[1])

abc = ["a", "b", "c"]


letter = abc.index(horizontal)
number = vertical -1
        
#print(map[1][1])

map[letter][number] = "X"
print(f"{line1}\n{line2}\n{line3}")






'''print(letter)
print(number)

if horizontal != "a" or "b" or "c":
    print("not on map")
elif vertical != 1 or 2 or 3:
    print("not on map")
'''



'''
if letter != 0 or 1 or 2:
        print("Not on map")
elif number != 0 or 1 or 2:
    print("Not on map")'''