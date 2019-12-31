def classify(number):
    # declare aliquont sum variable = 0
    # iterate over the numbers from end not including the number itself:
    # check if number % num == 0
    # add it to aliquont sum

    # if to total sum is equal to number:
    # perfect
    # if less:
    # deficient
    # if more:
    # abundant
    aliquont_sum = 0

    divisor = number - 1

    while divisor > 0:
        if number % divisor == 0:
            aliquont_sum += divisor
        divisor -= 1
    print(aliquont_sum)

    if number == aliquont_sum:
        print('perfect')
    elif number > aliquont_sum:
        print('deficient')
    else:
        print('abundant')


classify(33550336)
