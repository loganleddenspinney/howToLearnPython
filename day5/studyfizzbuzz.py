x = ""
for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        x = "FizzBuzz"
        print(x)
    elif number % 3 == 0:
            x = "Fizz"
            print(x)
    elif number % 5 == 0:
            x = "Buzz"
            print(x)
    else:
        print(number)
