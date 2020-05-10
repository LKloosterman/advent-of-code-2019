input = "168630-718098".split("-")

possible_password_count = 0

for password in range(int(input[0]), int(input[1])):
    digit_twins_flag = False
    decrease_flag = False

    last_digit = "-1"

    for digit in str(password):
        if digit == last_digit:
            digit_twins_flag = True
        elif digit < last_digit:
            decrease_flag = True

        last_digit = digit

    if digit_twins_flag == True and decrease_flag == False:
        possible_password_count += 1

print(possible_password_count)
