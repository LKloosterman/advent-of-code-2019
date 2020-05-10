# This range is our input of possible passwords
input = "168630-718098".split("-")

# This is the number of possible passwords we've found in the range
possible_password_count = 0

# Loop through all the numbers in the range to test
for password in range(int(input[0]), int(input[1])):
    # Gets set when we find at least two of the same number beside eachother
    digit_twins_flag = False
    # Gets set when we find a number which decreases from the last in the
    # sequence
    decrease_flag = False

    # Holds the last digit come across
    last_digit = "-1"

    # Loops through each digit of the password being tested
    for digit in str(password):
        # If the digit is equal to the last one found, set the twins flag
        if digit == last_digit:
            digit_twins_flag = True
        # If the digit is less than the last one found, set the decrease flag
        elif digit < last_digit:
            decrease_flag = True

        # Set the last_digit variable for the next loop iteration
        last_digit = digit

    # If we found two of the same numbers beside eachother, and none of the
    # numbers in the sequence decrease, add one to the possible password count
    if digit_twins_flag == True and decrease_flag == False:
        possible_password_count += 1

# Print the resulting number of possible passwords
print(possible_password_count)
