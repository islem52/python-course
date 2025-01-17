import statistics
import os

user_list = []

# Load existing list from file if it exists
filename = "user_list.txt"
if os.path.exists(filename):
    with open(filename, 'r') as file:
        user_list = [float(line.strip()) for line in file.readlines()]

while True:
    user_input = input("Enter a number (0 to quit): ")
    try:
        number = float(user_input)
        if number == 0:
            break
        user_list.append(number)
        
        # Print current and sorted lists
        print("Current List:", user_list)
        order = input("Sort in ascending or descending order? (a/d): ").lower()
        if order == 'd':
            print("Sorted List:", sorted(user_list, reverse=True))
        else:
            print("Sorted List:", sorted(user_list))

        # Calculate and display statistics
        print("Mean:", statistics.mean(user_list))
        print("Median:", statistics.median(user_list))

    except ValueError:
        print("Please enter a valid number.")

# Save the list to a file
with open(filename, 'w') as file:
    for number in user_list:
        file.write(f"{number}\n")
print("List saved to", filename)
