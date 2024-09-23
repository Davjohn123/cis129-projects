# Module 4 Lab-4 
# David Johnson 
# 9/20/24 
# what the program does is it gets the monthly sales from the user
# then it calculates if it was high enough for a store bonus
# then it the program gets the sales increase from the user
# then it calculates if the sales increase is high enough for a employee bonus
# lastly it prints the total store bonus and employee bouns and if they both max it congratulates you 

# declare local variables 
storeAmount = 0
empAmount = 0
salesIncrease = 0
monthlySales = 0

# This code gets the monthly sales 
monthlySales = float(input("The Monthly Sales Were\n"))

# This code determines the storeAmount bonus
if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else:
    StoreAmount = 0

# This code gets the percent of increase in sales 
salesIncrease = float(input("What was the % increase in sales\n")) 
salesIncrease = salesIncrease / 100

# This code determines the empAmount bonus 
if salesIncrease >= 0.05:
     empAmount = 75 
elif salesIncrease >= 0.04:
     empAmount = 50 
elif salesIncrease >= 0.03:
     empAmount = 40
else:
     empAmount = 0

# This code prints the bonus information 
print("The store bonus amount is $", storeAmount) 
print("The employee bonus amount is $", empAmount) 
if (storeAmount == 6000 ) & (empAmount == 75):
    print('Congrats! You have reached the highest bonus amounts possible! ') 
