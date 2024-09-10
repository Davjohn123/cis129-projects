# any * signs are to make it look like a receipt 
print ('************************************************')
print ('My Coffee and Muffin Shop')
# this is asking the user for the number of coffees and muffins they want and tey input it on a new line
muffins = input('Number of muffins bought\n')
muffins = int(muffins)
coffees = input('Number of coffees bought\n')
coffees = int(coffees)
print ('************************************************')
print ('')

#this is calculating the total cost for both the muffins and the coffee and also calculating the tax
muffincost = muffins * 4
coffeecost = coffees * 5
tax = (muffincost + coffeecost) * 0.06
print ('************************************************')
print ('My Coffee and Muffin Shop Receipt')
#this displays the cost to the user
print ('', coffees, "Coffee at $5 each: $", coffeecost)
print ('', muffins, "Coffee at $5 each: $", muffincost)
print ('6% tax: $', tax)
print ('---------')
# this adds the total cost of everything together
print ('Total: $', muffincost + coffeecost + tax)
print ('************************************************')
