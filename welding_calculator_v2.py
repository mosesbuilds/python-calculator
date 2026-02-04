price = float(input("Enter price per unit: "))
quantity = float(input("Enter quantity needed: "))
profit_percentage = float(input("Enter desired profit percentage: "))

total = price * quantity
profit = total * (profit_percentage / 100)
final_price = total + profit

print("-----------")
print("Total cost: ", total)
print("Profit: ", profit)
print("Final price to charge: ", final_price)
print("Thank you for using Moses Welding Calculator V2")