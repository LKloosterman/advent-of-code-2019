def find_occupied_coordinates(wire_path):
    occupied_coordinates = []
    current_coordinates = [0, 0]

    for path_instruction in wire_path.split(","):
        instruction_direction = path_instruction[:1]
        instruction_step_count = int(path_instruction[1:])
            
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

def find_overlap_coordinates(coordinate_set_one, coordinate_set_two):
    overlap_coordinates = []

    for coordinates in coordinate_set_one:
        if coordinates in coordinate_set_two:
            overlap_coordinates.append(coordinates.copy())
    
    return overlap_coordinates

def find_steps_to_reach(wire_path, target_coordinates):
    steps_taken = 0
    current_coordinates = [0, 0]

    for path_instruction in wire_path.split(","):
        instruction_direction = path_instruction[:1]
        instruction_step_count = int(path_instruction[1:])
            
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

            if current_coordinates == target_coordinates:
                break

        if current_coordinates == target_coordinates:
            break
    
    return steps_taken

first_wire_occupied_coordinates = []
second_wire_occupied_coordinates = []

wire_paths_file = open("input.txt", "r")

first_wire_path = wire_paths_file.readline()
second_wire_path = wire_paths_file.readline()

first_wire_occupied_coordinates = find_occupied_coordinates(first_wire_path)
second_wire_occupied_coordinates = find_occupied_coordinates(second_wire_path)

overlap_coordinates = find_overlap_coordinates(first_wire_occupied_coordinates,
        second_wire_occupied_coordinates)

lowest_step_count = 0

for coordinates in overlap_coordinates:
    total_steps_required = find_steps_to_reach(first_wire_path, coordinates) \
            + find_steps_to_reach(second_wire_path, coordinates)

    if total_steps_required < lowest_step_count or lowest_step_count == 0:
        lowest_step_count = total_steps_required

print(lowest_step_count)
