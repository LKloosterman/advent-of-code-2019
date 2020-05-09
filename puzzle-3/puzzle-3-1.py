# This function takes record of all the coordinates a wire passes through, and
# returns that record as a list
def find_occupied_coordinates(wire_path):
    occupied_coordinates = []
    current_coordinates = [0, 0]

    # Loop through the instructions for the wire's path
    for path_instruction in wire_path.split(","):
        # Parse the instruction to figure out the direction and number of steps
        instruction_direction = path_instruction[:1]
        instruction_step_count = int(path_instruction[1:])
            
        # Loop through the number of steps and add each coordinate passed
        for _i in range(instruction_step_count):
            if instruction_direction == "U":
                current_coordinates[1] += 1
            elif instruction_direction == "D":
                current_coordinates[1] -= 1
            elif instruction_direction == "L":
                current_coordinates[0] -= 1
            elif instruction_direction == "R":
                current_coordinates[0] += 14

            occupied_coordinates.append(current_coordinates.copy())
    
    return occupied_coordinates

# This function finds matching coordinates in both coordinate sets, and returns
# a list of coordinates found in both sets, which will be the coordinates
# where two wires overlap for the puzzle
def find_overlap_coordinates(coordinate_set_one, coordinate_set_two):
    overlap_coordinates = []

    # Loop through each coordinate in the first set, check if it exists in the
    # second set. If so, add it to the set of found overlaps
    for coordinates in coordinate_set_one:
        if coordinates in coordinate_set_two:
            overlap_coordinates.append(coordinates.copy())
    
    return overlap_coordinates

# This function calculates the manhattan distance of each coordinate in the
# given set to the coordinate 0, 0 (the central port). Since we're checking the
# distance to 0, 0 we can just add the absolute values of a given coordinate
# instead of first subtracting the x or y of the target coordinate respectively
def find_lowest_manhattan_distance(coordinate_set):
    lowest_manhattan_distance = 0

    # Loop through the coordinates in the given set and find the lowest
    # manhattan distance
    for coordinates in coordinate_set:
        overlap_manhattan_distance = abs(coordinates[0]) + abs(coordinates[1])

        if overlap_manhattan_distance < lowest_manhattan_distance \
                or lowest_manhattan_distance == 0:
            lowest_manhattan_distance = overlap_manhattan_distance
    
    return lowest_manhattan_distance
    
# The list of occupied coordinates for each wire
first_wire_occupied_coordinates = []
second_wire_occupied_coordinates = []

# Open the input file and take both wire path instructions into memory
wire_paths_file = open("input.txt", "r")
first_wire_path = wire_paths_file.readline()
second_wire_path = wire_paths_file.readline()

first_wire_occupied_coordinates = find_occupied_coordinates(first_wire_path)
second_wire_occupied_coordinates = find_occupied_coordinates(second_wire_path)

overlap_coordinates = find_overlap_coordinates(first_wire_occupied_coordinates,
        second_wire_occupied_coordinates)

# Print the resulting lowest manhattan distance
print(find_lowest_manhattan_distance(overlap_coordinates))
