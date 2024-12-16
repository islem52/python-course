clients = int(input("How many people need a ride ? :"))
maximum = int(input("How many people can one Taxi fit at once ? :"))


fullTaxis = clients//maximum
lastTaxi = clients%maximum


print(f"you will have {fullTaxis} full car(s) and an additional car that will contain {lastTaxi} client(s)")