def is_armstrong_number(number):

    # determine how many digits in the input = power to raise
    # convert input to string and get its len
    # declare sum variable
    # iterate over the stringified input
    # covert each char to int and raise to the power
    # add it to sum variable
    # if total sum is equal to input
    # return True
    # else False
    string_num = str(number)
    power = len(string_num)
    total_sum = 0

    for digit in string_num:
        total_sum += int(digit) ** power
        print(total_sum)
    if total_sum != number:
        return False
    return True


print(is_armstrong_number(153))
