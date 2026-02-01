try:
    price = float(input("Enter price per unit: "))
    quantity = float(input("Enter quantity needed: "))
    profit_percent = float(input("Enter desired profit percentage: "))

    total_cost = price * quantity
    profit = total_cost * (profit_percent / 100)
    final_price = total_cost + profit

    print("\n-----------")
    print("Total cost: ", total_cost)
    print("Profit: ", profit)
    print("Final price to charge: ", final_price)
    print("Thank you for using Moses Welding Calculator V2")

except ValueError:
    print("Invalid input! Please enter numbers only.")