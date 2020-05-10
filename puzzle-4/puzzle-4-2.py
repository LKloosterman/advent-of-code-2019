# This range is our input of possible passwords
input = "168630-718098".split("-")

# This is the number of possible passwords we've found in the range
possible_password_count = 0

# Loop through all the numbers in the range to test
for password in range(int(input[0]), int(input[1])):
    # Gets set when we're sure none of the numbers decrease in the sequence
    ok_decrease_flag = True
    # Gets set when we find two and only two of a number in succession
    found_twin_digits = False

    # Counts the number of same digits come across
    consecutive_digit_count = 1

    # Holds the previous digit tested
    last_digit = "0"

    # Loops through each digit of the password being tested
    for digit in str(password):
        # If the digit is equal to the last one found, add one to the
        # consecutive digits counter
        if digit == last_digit:
            consecutive_digit_count += 1
        # If the digit is less than the previous one, set the decrease flag to
        # False so we know this password is not valid
        elif digit < last_digit:
            ok_decrease_flag = False
        else:
            # If the digit is new, and the digit counter is exactly 2, it means
            # we've found a pair of digits (two and only two consecutive), so we
            # set the found_twin_digits flag
            if consecutive_digit_count == 2:
                found_twin_digits = True
            
            # Reset the consecutive digit count now that we've come across a new
            # number
            consecutive_digit_count = 1

        # Set the last_digit variable for the next loop iteration
        last_digit = digit

    # Check whether the last digit made a pair of exactly 2 for a last chance to
    # find a pair
    if consecutive_digit_count == 2:
        found_twin_digits = True

    # If we found two and only two numbers beside eachother, and none of the
    # numbers in the sequence decrease, add one to the possible password count
    if found_twin_digits and ok_decrease_flag:
        possible_password_count += 1

# Print the resulting number of possible passwords    
print(possible_password_count)
