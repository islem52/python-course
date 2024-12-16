
# Get ages from the user
age1 = int(input("Please type in the age of the first person: "))
age2 = int(input("Please type in the age of the second person: "))

# Compare ages and print the result
if age1 > age2:
    print(f"The older age is: {age1}")
elif age2 > age1:
    print(f"The older age is: {age2}")
else:
    print("Both people are the same age!")
