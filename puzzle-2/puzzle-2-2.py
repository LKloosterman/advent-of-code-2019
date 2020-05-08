def add_values(value_one, value_two):
    return str(int(value_one) + int(value_two))

def multiply_values(value_one, value_two):
    return str(int(value_one) * int(value_two))

program_file = open("input.txt", "r")
program = program_file.readline()
lexed_program = program.split(",")

current_inputs = ["0", "0"]
inputs_found = False

while inputs_found != True:
    halt = False
    execution_index = 0

    while halt != True:
        if lexed_program[execution_index] == "1":
            lexed_program[int(lexed_program[execution_index + 3])] = add_values(
                lexed_program[int(lexed_program[execution_index + 1])],
                lexed_program[int(lexed_program[execution_index + 2])]
            )

        elif lexed_program[execution_index] == "2":
            lexed_program[int(lexed_program[execution_index + 3])] = multiply_values(
                lexed_program[int(lexed_program[execution_index + 1])],
                lexed_program[int(lexed_program[execution_index + 2])]
            )

        elif lexed_program[execution_index] == "99":
            halt = True
        
        execution_index += 4
    
    print(lexed_program[1] + ", " + lexed_program[2] + ": " + lexed_program[0])
    
    if lexed_program[0] == "19690720":
        inputs_found = True
    else:
        if current_inputs[1] == "99":
            current_inputs[1] = "0"
            current_inputs[0] = str(int(current_inputs[0]) + 1)
        else:
            current_inputs[1] = str(int(current_inputs[1]) + 1)
        
        lexed_program = program.split(",")
        lexed_program[1] = current_inputs[0]
        lexed_program[2] = current_inputs[1]
