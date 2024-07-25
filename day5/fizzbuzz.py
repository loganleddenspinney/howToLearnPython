start = 0
for i in range(1, 101):
    start = i
    if i % 3 == 0 and i % 5 != 0:
        start = "Fizz"
    elif i % 5 == 0 and i % 3 != 0:
        start = "Buzz"
    elif i % 3 == 0 and i % 5 == 0:
        start = "FizzBuzz"
        
    print(start)
        

