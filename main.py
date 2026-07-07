inventory = {}

while True:
    print("\n===================================")
    print("     Inventory Management System")
    print("===================================")

    print("1. Add Product")
    print("2. View Products")
    print("3. Update Stock")
    print("4. Delete Product")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        product = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))

        inventory[product] = quantity
        print("Product added successfully!")

    elif choice == "2":
        if inventory:
            print("\nInventory:")
            for product, quantity in inventory.items():
                print(product, ":", quantity)
        else:
            print("Inventory is empty.")

    elif choice == "3":
        product = input("Enter product name: ")

        if product in inventory:
            quantity = int(input("Enter new quantity: "))
            inventory[product] = quantity
            print("Stock updated successfully!")
        else:
            print("Product not found.")

    elif choice == "4":
        product = input("Enter product name to delete: ")

        if product in inventory:
            del inventory[product]
            print("Product deleted successfully!")
        else:
            print("Product not found.")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid Choice")
