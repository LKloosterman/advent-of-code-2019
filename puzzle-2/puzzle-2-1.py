def add_values(value_one, value_two):
    return str(int(value_one) + int(value_two))

def multiply_values(value_one, value_two):
    return str(int(value_one) * int(value_two))

program_file = open("input.txt", "r")
program = program_file.readline()
lexed_program = program.split(",")

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

print(lexed_program[0])
