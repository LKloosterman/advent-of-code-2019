import math

def calculate_fuel(mass):
    return math.floor(int(mass) / 3) - 2

total_fuel_requirement = 0

file_stream = open("input.txt", "r")

for line in file_stream:
    total_fuel_requirement += calculate_fuel(line)

print(total_fuel_requirement)
