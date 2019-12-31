def is_armstrong_number(number):


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
