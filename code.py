import math


Pennies = input("Please enter your number of pennies: ")
Pennies = int(Pennies)
print("Total:" , Pennies)

Dollar_Bills = 100
Nickels = 5 
Dimes = 10   
Quarters = 25    
p_in_pen = 1


num_of_dollars = Pennies // Dollar_Bills
print("Dollars:" , num_of_dollars)

the_change = Pennies % Dollar_Bills

num_of_quarters = the_change // Quarters
print("Quarters:" , num_of_quarters)

the_change = Pennies % Quarters

num_of_dimes = the_change // Dimes
print("Dimes:" , num_of_dimes)

the_change = Pennies % Dimes

num_of_nickels = the_change // Nickels
print("Nickels:" , num_of_nickels)

the_change = Pennies % Nickels

num_of_pennies =the_change // p_in_pen
print("Pennies:" , num_of_pennies)

the_change = num_of_pennies % p_in_pen
