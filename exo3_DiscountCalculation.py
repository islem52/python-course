from enum import Enum
class Days(Enum):
    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"


totalAmount = int(input("enter the total amount:"))
itemsNb = int(input("enter the number of items:"))


cond = False
discount = False


while not cond :
    day = str(input("Day of the week : "))
    if day.upper() in Days:
        cond = True
        if day.upper() in [Days.SATURDAY,Days.SUNDAY]:
            discount = True

if discount :
    if itemsNb > 5 :
        totalAmount = totalAmount - (totalAmount * 0.25)
    else : totalAmount = totalAmount - (totalAmount * 0.2)
    print(f"Total price after discount is {totalAmount}$")
else:
    print(f"Total price is {totalAmount}$")