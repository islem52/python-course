name = input("Please enter your status (VIP or regular): ")
ticketPrice = 15.50

if name != "VIP" or name != "vip":
    ticketNumber = input("How many tickets do you want to buy?\n")
    print(f"The total cost is {ticketNumber*ticketPrice}\nEnjoy your tickets")
else:
    print("Enjoy the show for free!!")


