cities = {}

while True:
    city_name = input("Enter the name of a city (or type 'stop' to finish): ")
    if city_name.lower() == 'stop':
        break
    population = len(city_name) * 1000000
    cities[city_name] = population

# Sort cities by population
sorted_cities = sorted(cities.items(), key=lambda item: item[1], reverse=True)

# Print the results
for city, population in sorted_cities:
    print(f"{city}: {population} citizens")
