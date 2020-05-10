import regex

input = "168630-718098".split("-")

possible_password_count = 0

for password in range(int(input[0]), int(input[1])):
    ok_decrease_flag = True
    found_twin_digits = False

    consecutive_digit_count = 1

    last_digit = "0"

    for digit in str(password):
        if digit == last_digit:
            consecutive_digit_count += 1
        elif digit < last_digit:
            ok_decrease_flag = False
        else:
            if consecutive_digit_count == 2:
                found_twin_digits = True
            
            consecutive_digit_count = 1

        last_digit = digit

    if consecutive_digit_count == 2:
        found_twin_digits = True

    if found_twin_digits and ok_decrease_flag:
        possible_password_count += 1
    
print(possible_password_count)
