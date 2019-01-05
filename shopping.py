
item_name_1 = input('Name your first item')
item_name_2 = "shampoo"
item_name_3 = "chicken"
item_name_4 = "yogurt"
item_name_5 = "carrots"

item_price_1 = 1.00
item_price_2 = 1.99
item_price_3 = 6.99
item_price_4 = 1.99
item_price_5 = 2.99

item_quant_1 = 5
item_quant_2 = 1
item_quant_3 = 4
item_quant_4 = 3
item_quant_5 = 2

total_cost_1 = item_quant_1 * item_price_1
total_cost_2 = item_quant_2 * item_price_2
total_cost_3 = item_quant_3 * item_price_3
total_cost_4 = item_quant_4 * item_price_4
total_cost_5= item_quant_5 * item_price_5

total_items= item_quant_1 + item_quant_2 +item_quant_3 +item_quant_4 + item_quant_5
tax = .0825

total_grocery_cost = (total_cost_1 + total_cost_2 + total_cost_3 + total_cost_4 + total_cost_5)*tax + (total_cost_1 + total_cost_2 + total_cost_3 + total_cost_4 + total_cost_5)
#   need to use the f formatted string since you have strings and numbers. Mismatched data types



apple = f"{item_quant_1} {item_name_1} = {total_cost_1}"
shampoo = f"{item_quant_2} {item_name_2} = {total_cost_2}"
chicken = f"{item_quant_3} {item_name_3} = {total_cost_3}"
yogurt = f"{item_quant_4} {item_name_4} = {total_cost_4}"
carrot = f"{item_quant_5} {item_name_5} = {total_cost_5}"
print(apple)
print(shampoo)
print(chicken)
print(yogurt)
print(carrot)
print(total_items)
print(total_grocery_cost)
