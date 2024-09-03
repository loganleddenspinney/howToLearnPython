def calculate_love_score(name_1, name_2):
    x = (name_1+name_2).lower()
    y = 0
    z = 0
    for i in x:
        if i == "t":
            y +=1
        elif i == "r":
            y +=1
        elif i == "u":
            y+=1
        elif i == "e":
            y+=1
            z+=1
        elif i == "l":
            z+=1
        elif i == "o":
            z+=1
        elif i == "v":
            z+=1

            
    a = str(y)+str(z)
    print(int(a))

            

calculate_love_score("Angela Yu", "Jack Bauer")