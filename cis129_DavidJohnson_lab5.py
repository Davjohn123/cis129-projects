totalBottles = 0
counter = 1
todayBottles = 0
totalPayout = 0
keepGoing = "y"
while counter < 8:
   todayBottles = input (f'Enter number bottles for day #{counter}: ')
   todayBottles= int(todayBottles)
   totalBottles = todayBottles + totalBottles
   totalPayout = 0.10 * totalBottles
   round (totalPayout, 2)
   counter += 1
   if counter == 8:
      print (f'Total number of bottles sold was {totalBottles} and the total payout was {totalPayout:.2f}')
      print ("")
      keepGoing = input ("Do you want to enter another week’s worth of data?\n Enter y or n\n")
      if keepGoing == 'y':
         counter = 1
