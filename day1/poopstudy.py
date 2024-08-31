class Band:
  
   def bandName(self):
       homeTown = input("Name of your hometown")
       pet = input("Name of your pet")
       result = homeTown +  " " + pet
       print(result)
       return(result)
  


answer = Band()
answer.bandName()
