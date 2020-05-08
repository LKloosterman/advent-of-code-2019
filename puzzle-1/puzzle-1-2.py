import math

def calculate_fuel(mass):
    fuel_requirement = math.floor(int(mass) / 3) - 2
    
    if fuel_requirement <= 0:
        return 0
    else:
        return fuel_requirement + calculate_fuel(fuel_requirement)

total_fuel_requirement = 0

file_stream = open("input.txt", "r")

for line in file_stream:
    total_fuel_requirement += calculate_fuel(line)

print(total_fuel_requirement)
