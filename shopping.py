import math

#empty list of item prices
item_prices = []
#tax
tax = .0825
#input request from user
num_items = int(input('How many items?'))
#for loop running based on number of items user entered
for i in range (0, num_items):
  name = str(input('Enter name of item:'))
  price= float(input('Enter price of item:'))
  quantity= int(input('Enter quanity of item:'))
  item_prices.append(price)
#get sum of the prices entered by user
total =sum(item_prices)
tax = .0825
tax += total *tax
final_total = tax + total

sumTotal = f"Your total is {total}"
the_tax = f"Tax is {tax}"
final = f"Total total is: {final_total}"
#return the sum, tax, and total with taxt
print(sumTotal)
print(the_tax)
print(final)




