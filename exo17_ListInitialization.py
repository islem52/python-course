# Initialize empty lists
numbers = []
shoe_sizes = []

for num in [1, 2, 3, 4, 5, 2, 3]: 
    if num not in numbers:
        numbers.append(num)

# Append values to shoe_sizes list using a loop
for size in range(8, 13):
    shoe_sizes.append(size)

# Combine numbers and shoe_sizes into a third list
combined_list = numbers + shoe_sizes

# Print all lists
print("Numbers List:", numbers)
print("Shoe Sizes List:", shoe_sizes)
print("Combined List:", combined_list)
