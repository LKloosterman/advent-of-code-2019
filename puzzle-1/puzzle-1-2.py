import math

# This function calculates the mass needed for the given module mass, this is
# the same function as the one in the part 1 solution, but has been
# made recursive in order to account for the mass of the fuel added as well
# (requirement for part 2 of the puzzle).
def calculate_fuel(mass):
    # Do the initial fuel requirement calculation
    fuel_requirement = math.floor(int(mass) / 3) - 2
    
    if fuel_requirement <= 0:
        # If the result would not add any more extra fuel, return 0 and unravel the
        # call stack to finally return the overal result back to the main program
        return 0
    else:
        # If there's still fuel needed to account for the last amount of fuel
        # added, we'll need to calculate the amount of extra fuel to add in
        # order to support this added fuel!
        return fuel_requirement + calculate_fuel(fuel_requirement)

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
