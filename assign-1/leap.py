startyear=int(input("Enter your starting year: "))
rangeyear=int(input("Enter your range: "))

endyear=startyear + rangeyear 

currentyear=startyear

print(f"leap year from {startyear} to {endyear} is: ")

while currentyear <= endyear:
  if(currentyear % 4 == 0):
      print(currentyear)

  currentyear += 1 
            
