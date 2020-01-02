def classify(number):

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
# this function is O(n) and needs to be done faster

classify(33550336)
