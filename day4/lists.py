fruits = ["cherry", "apple", "pear"]

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]


#to alter the list you can do somwthing like this:
#states_of_america[1] = "Pencilvania"
#then if you print the list Pennsylvania will have its spelling changed to Pencilvania.

#to add something to the list you can do: 

#states_of_america.append("Logansstatebitch")

#to add one item

#to add more items you can do this:

#states_of_america.extend(["loganland", "johnsmithland"])

#to find how many states in america do:
#print(len(states_of_america))

#NESTED LISTS

vegetables = ["spinach", "kale", "celery"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)

print(f"{states_of_america[0]} is the first founded state in the USA")

print(dirty_dozen[1][1])