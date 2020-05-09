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
                current_coordinates[0] += 1

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

# This function counts the steps it takes a wire path to reach a given
# coordinate by following the path instructions until it gets to the coordinate
def find_steps_to_reach(wire_path, target_coordinates):
    steps_taken = 0
    current_coordinates = [0, 0]

    # Loop through the instructions for the wire's path
    for path_instruction in wire_path.split(","):
        # Parse the instruction to figure out the direction and number of steps
        instruction_direction = path_instruction[:1]
        instruction_step_count = int(path_instruction[1:])
            
        # Loop through the number of steps and add a step for each coordinate
        # passed
        for _i in range(instruction_step_count):
            if instruction_direction == "U":
                current_coordinates[1] += 1
            elif instruction_direction == "D":
                current_coordinates[1] -= 1
            elif instruction_direction == "L":
                current_coordinates[0] -= 1
            elif instruction_direction == "R":
                current_coordinates[0] += 1
            
            steps_taken += 1

            # Break the inner loop when we get to our target coordinates
            if current_coordinates == target_coordinates:
                break

        # Break the outer loop when we get to our target coordinates
        if current_coordinates == target_coordinates:
            break
    
    return steps_taken

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

# The lowest amount of steps needed to reach any overlap
lowest_step_count = 0

# Loop through the found overlapping coordinates and find the one that requires
# the least amount of steps to reach
for coordinates in overlap_coordinates:
    total_steps_required = find_steps_to_reach(first_wire_path, coordinates) \
            + find_steps_to_reach(second_wire_path, coordinates)

    if total_steps_required < lowest_step_count or lowest_step_count == 0:
        lowest_step_count = total_steps_required

# Print the resulting lowest step count
print(lowest_step_count)
