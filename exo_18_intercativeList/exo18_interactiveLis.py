
import pathlib

def display_menu():
    print("\nMenu:")
    print("1. Append")
    print("2. Insert")
    print("3. Pop")
    print("4. Remove")
    print("5. Sort")
    print("6. Reverse")
    print("7. Search")
    print("8. Save List to File")
    print("9. Load List from File")
    print("10. Quit")


# Initialize the list
numbers = [1, 2, 3, 4, 5]
print("Initial List:", numbers)

while True:
    display_menu()
    try:
        choice = int(input("Choose an option: "))
        if choice == 1:  # Append
            value = float(input("Enter value to append: "))
            numbers.append(value)
            print("Updated List:", numbers)

        elif choice == 2:  # Insert
            value = float(input("Enter value to insert: "))
            index = int(input(f"Enter index (0 to {len(numbers)}): "))
            if 0 <= index <= len(numbers):
                numbers.insert(index, value)
                print("Updated List:", numbers)
            else:
                print("Error: Index out of range.")

        elif choice == 3:  # Pop
            if numbers:
                index = int(input(f"Enter index to pop (0 to {len(numbers) - 1}): "))
                if 0 <= index < len(numbers):
                    popped_value = numbers.pop(index)
                    print(f"Popped Value: {popped_value}")
                    print("Updated List:", numbers)
                else:
                    print("Error: Index out of range.")
            else:
                print("Error: List is empty.")

        elif choice == 4:  # Remove
            if numbers:
                value = float(input("Enter value to remove: "))
                if value in numbers:
                    numbers.remove(value)
                    print("Updated List:", numbers)
                else:
                    print("Error: Value not found in the list.")
            else:
                print("Error: List is empty.")

        elif choice == 5:  # Sort
            numbers.sort()
            print("List sorted.")
            print("Updated List:", numbers)

        elif choice == 6:  # Reverse
            numbers.reverse()
            print("List reversed.")
            print("Updated List:", numbers)

        elif choice == 7:  # Search
            value = float(input("Enter value to search: "))
            if value in numbers:
                index = numbers.index(value)
                print(f"Value found at index: {index}")
            else:
                print("Value not found in the list.")

        elif choice == 8:  # Save List to File
            script_dir = pathlib.Path(__file__).parent  # Directory of the script
            filename = input("Enter filename to save the list: ")
            if "/" in filename or "\\" in filename:
                print("Error: Do not include paths, only filenames.")
                continue
            filepath = script_dir / filename
            with open(filepath, "w") as file:
                file.write(" ".join(map(str, numbers)))
            print(f"List saved to {filepath}")

        elif choice == 9:  # Load List from File
            script_dir = pathlib.Path(__file__).parent  # Directory of the script
            filename = input("Enter filename to load the list: ")
            if "/" in filename or "\\" in filename:
                print("Error: Do not include paths, only filenames.")
                continue
            filepath = script_dir / filename
            try:
                with open(filepath, "r") as file:
                    numbers = list(map(float, file.read().split()))
                print(f"List loaded from {filepath}")
                print("Updated List:", numbers)
            except FileNotFoundError:
                print("Error: File not found in the script's directory.")

        elif choice == 10:  # Quit
            print("Exiting program.")
            break

        else:
            print("Error: Invalid choice. Please select a valid option.")

    except ValueError:
        print("Error: Please enter a valid number.")
