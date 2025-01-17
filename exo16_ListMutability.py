numbers = [1, 2, 3, 4, 5]

while True:
    try:
        index = int(input("Enter index (-1 to quit): "))
        if index == -1:
            break
        if index < 0 or index >= len(numbers):
            print("Invalid index. Please try again.")
            continue
        try:
            new_value = float(input("Enter new value: "))  # Allow float for new value
            numbers[index] = new_value
            print([int(x) if x.is_integer() else x for x in numbers])#manage numbers like 1.0 ,2.00
        except ValueError:
            print("Please enter a valid float for the new value.")
    except ValueError:
        print("Please enter a valid integer for the index.")
