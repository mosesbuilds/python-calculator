def welding_calculator_v2():
    print("\nMoses Welding Calculator V2")

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

    input("\nPress Enter to return to menu...")
def basic_calculator():
    print("\nBasic Welding Calculator")
    price = float(input("Enter price per unit: "))
    quantity = float(input("Enter quantity needed: "))
    total = price * quantity
    print("Total cost is:", total)
    input("Press Enter to return to menu...")


def project_cost():
    print("\nProject Cost Calculator")

    material = float(input("Material cost: "))
    labor = float(input("Labor cost: "))

    base = material + labor

    profit = base * 0.15      # 15% profit
    tax = base * 0.075        # 7.5% tax on base only

    final_price = base + profit + tax

    print("\n--- Project Summary ---")
    print("Base cost:", base)
    print("Profit (15%):", profit)
    print("Tax (7.5% on base):", tax)
    print("Final price to charge:", final_price)

    input("\nPress Enter to return to menu...")


def daily_log():
    print("\nDaily Welding Log")
    job = input("Enter job name: ")
    earnings = float(input("Enter earnings: "))
    print("Job:", job)
    print("Earnings:", earnings)
    input("Press Enter to return to menu...")


while True:
    print("\n==== Moses Welding Tools ====")
    print("1. Basic Welding Calculator")
    print("2. Project Cost Calculator")
    print("3. Daily Welding Log")
    print("4. Moses Welding Calculator V2")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        basic_calculator()
    elif choice == "2":
        project_cost()
    elif choice == "3":
        daily_log()
    elif choice == "4":
        welding_calculator_v2()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option selected. Try again.")