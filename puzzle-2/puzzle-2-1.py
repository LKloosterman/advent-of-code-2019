# This function adds together two integer values given as strings and returns
# the result as a string
def add_values(value_one, value_two):
    return str(int(value_one) + int(value_two))

# This function multiplies two integer values given as strings and returns the
# result as a string
def multiply_values(value_one, value_two):
    return str(int(value_one) * int(value_two))

# Open the input file and take the entire program text into program as a string
program_file = open("input.txt", "r")
program = program_file.readline()

# Split the given program string into a list to seperate each value
lexed_program = program.split(",")

# Whether or not a code 99 (halt code) has been reached
halt = False
# The current index to look for the next instruction
execution_index = 0

while halt != True:
    # If we find a code 1 instruction, add together the values at the location
    # specified in the operation parameters (next two numbers), and save the
    # result at the location specified in the last parameter
    if lexed_program[execution_index] == "1":
        lexed_program[int(lexed_program[execution_index + 3])] = add_values(
            lexed_program[int(lexed_program[execution_index + 1])],
            lexed_program[int(lexed_program[execution_index + 2])]
        )

    # If we find a code 2 instruction, add together the values at the location
    # specified in the operation parameters (next two numbers), and save the
    # result at the location specified in the last parameter
    elif lexed_program[execution_index] == "2":
        lexed_program[int(lexed_program[execution_index + 3])] = multiply_values(
            lexed_program[int(lexed_program[execution_index + 1])],
            lexed_program[int(lexed_program[execution_index + 2])]
        )

    # If we find a code 99 instruction, break out of our loop
    elif lexed_program[execution_index] == "99":
        halt = True
    
    # Increment the instruction index by 4 to skip over the finished instruction
    # and it's parameters to find the next instruction
    execution_index += 4

# Print the final result, held in the first address of the program
print(lexed_program[0])
