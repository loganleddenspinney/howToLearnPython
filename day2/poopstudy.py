class calculator:


   def func(self):
       check = float(input("What is the total price of the check? "))
       tip = float(input("how much money are you leaving as a tip? "))
       split = int(input("How many people are splitting the check? "))
       totalBill = (check + check * (tip/100)) / split
       totalBill = "{:.2f}".format(totalBill)
       print(totalBill)
       return(totalBill)


answer = calculator()
answer.func()
