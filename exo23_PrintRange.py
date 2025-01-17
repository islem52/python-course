while True:
    user_input = input("Please enter a positive integer: ")
    try:
        N = int(user_input)
        if N <= 0:
            print("The number must be positive. Please try again.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

for number in range(-N, N + 1):
    if number != 0:
        print(number)
