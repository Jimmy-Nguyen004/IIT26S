print('Calculate fuel consumption')

Feed = input('Enter travel distance (kilometers): ')
Distance = int(Feed)

Feed = input('Enter fuel usage (liters): ')
FuelUsage = int(Feed)

Consumption = int(FuelUsage / Distance * 100)

print(f'Fuel consumption is {Consumption} l per 100 kilometers.')
