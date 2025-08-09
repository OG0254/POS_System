from records import read_file, write_file, append_file, delete_file
from report import search_file
from transactions import Stock


def show_menu():
    print("\n📌POS_Point_of_Sale_System")
    print("1. View file content")
    print("2. Overwrite file")
    print("3. Append to file")
    print("4. Delete file")
    print("5. Search file")
    print("6. Add new product")
    print("7. Exit")

file_path = "items.txt"

while True:
    show_menu()
    choice = input("Enter your choice (1–7): ")

    if choice == "1":
        read_file(file_path)

    elif choice == "2":
        content = input("Enter content to write (will overwrite file): ")
        write_file(file_path, content)

    elif choice == "3":
        append_file(file_path)

    elif choice == "4":
        confirm = input("Are you sure you want to delete the file? (yes/no): ")
        if confirm.lower() == "yes":
            delete_file(file_path)

    elif choice == "5":
        keyword = input("Enter keyword to search for: ")
        results = search_file(file_path, keyword)
        print("Search Results:")
        for result in results:
            print(result.strip())
            print("-" * 40)

    elif choice == "6":
        # ✅ Add new freelance project
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        stock = Stock(name, price)

        while True:
            product_name = input("Enter product name (or 'done' to finish): ")
            if product_name.lower() == "done":
                break
            amount = float(input(f"Amount for {product_name}: "))
            stock.name(name, amount)

        # Display summary
        print("\n--- Project Summary ---")
        stock.display_summary()

        # Save to file
        with open(file_path, "a") as f:
            f.write(f"\nProduct: 🎯{stock.name}\n")
            f.write(f"Product price: 💰{stock.price}\n")
            f.write("New stock:\n")
            for name, amount in stock.price:
                f.write(f"  {name}: {amount}\n")
            f.write(f"Total Expenses: 💸{stock.calculate_total()}\n")
            f.write("-" * 40 + "\n")
    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
