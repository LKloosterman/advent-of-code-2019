import math

# This small function calculates the fuel needed to support the given module
# mass using the formula given in the puzzle instructions
def calculate_fuel(mass):
    return math.floor(int(mass) / 3) - 2

# The total amount of required fuel needed for all module masses given in the
# input
total_fuel_requirement = 0

# Open the input file
file_stream = open("input.txt", "r")

# Iterate over each of the lines in the input file for each module mass and
# add the calculated fuel requirement to the total
for line in file_stream:
    total_fuel_requirement += calculate_fuel(line)

# Print the end result!
print(total_fuel_requirement)
