import math

#better shopping calculator with DRY code used to refactor
item_prices = []
tax = .0825
num_items = int(input('How many items?'))
for i in range (0, num_items):
  name = str(input('Enter name of item:'))
  price= float(input('Enter price of item:'))
  quantity= int(input('Enter quanity of item:'))
  item_prices.append(price)

total =sum(item_prices)
tax = .0825
tax += total *tax
final_total = tax + total

sumTotal = f"Your total is {total}"
the_tax = f"Tax is {tax}"
final = f"Total total is: {final_total}"

print(sumTotal)
print(the_tax)
print(final)



#first version without dry code
# #items for shopping list
# item_name_1 = input('What is first item name:')
# item_name_2 = input('What is second item name:')
# item_name_3 = input('What is item name:')
# item_name_4 = input('What is item name:')
# item_name_5 = input('What is item name:')

# #item prices
# item_price_1 = float(input("What is first item price:"))
# item_price_2 = float(input("What is second item price:"))
# item_price_3 = float(input("What is item price:"))
# item_price_4 = float(input("What is item price:"))
# item_price_5 = float(input("What is item price:"))

# #item quanity
# item_quant_1 = int(input("What is first item quantity:"))
# item_quant_2 = int(input("What is the second item quantity:"))
# item_quant_3 = int(input("What is the item quantity:"))
# item_quant_4 = int(input("What is the  itemquantity:"))
# item_quant_5 = int(input("What is the item quantity:"))

# total_cost_1 = item_quant_1 * item_price_1
# total_cost_2 = item_quant_2 * item_price_2
# total_cost_3 = item_quant_3 * item_price_3
# total_cost_4 = item_quant_4 * item_price_4
# total_cost_5= item_quant_5 * item_price_5

# total_items= item_quant_1 + item_quant_2 +item_quant_3 +item_quant_4 + item_quant_5
# tax = .0825

# total_grocery_cost = (total_cost_1 + total_cost_2 + total_cost_3 + total_cost_4 + total_cost_5)*tax + (total_cost_1 + total_cost_2 + total_cost_3 + total_cost_4 + total_cost_5)
# #   need to use the f formatted string since you have strings and numbers. Mismatched data types



# apple = f"{item_quant_1} {item_name_1} = {total_cost_1}"
# shampoo = f"{item_quant_2} {item_name_2} = {total_cost_2}"
# chicken = f"{item_quant_3} {item_name_3} = {total_cost_3}"
# yogurt = f"{item_quant_4} {item_name_4} = {total_cost_4}"
# carrot = f"{item_quant_5} {item_name_5} = {total_cost_5}"
# print(apple)
# print(shampoo)
# print(chicken)
# print(yogurt)
# print(carrot)
# print(total_items)
# print(round(total_grocery_cost))
