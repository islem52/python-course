valid = False

while valid == False:
    price = input("please enter the price in dinars :")
    try:
        price_float = float(price)
        if price_float > 0:
            valid = True
        else:
            print("enter a valid price\n")
    except ValueError:
        print("Please enter a valid number.")

integer_part = int(price_float)

# Split the price string to get the decimal part
decimal_part_str = price.split('.')[1] if '.' in price else '0'
decimal_part = int(decimal_part_str)

print(f"the integer part of the price is : {integer_part} dinars and the decimal part is : {decimal_part} Centimes")
