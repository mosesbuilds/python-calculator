while True:
    print("\n==== Moses Welding Tools ====")
    print("1. Basic Welding Calculator")
    print("2. Project Cost Calculator")
    print("3. Daily Welding Log")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Opening Basic Welding Calculator...")
    elif choice == "2":
        print("Opening Project Cost Calculator...")
    elif choice == "3":
        print("Opening Daily Welding Log...")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option selected. Try again.")