class if_practice:
    def ifelse(self):
        x = int(input("Check if number is even or odd "))
        if x % 2 == 0:
            print(f"{x} is even")
        else:
            print(f"{x} is odd")

answer = if_practice()
answer.ifelse()