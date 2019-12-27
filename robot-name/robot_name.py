import random
import string

class Robot(object):
    def __init__(self):  
        pass


    def reset(self):

        # define empty string - name
        # generate random uppercase letters 
        # append to string two of the generated letters
        # fill with random number from 100-999
        name = ''

        for _ in range(2):
            letters = random.choices(string.ascii_uppercase) # this generates list
            name += letters[0]

        for _ in range(3):
            digits = random.choices(string.digits)  # this generates list
            name += digits[0]
        return name



if __name__ == '__main__':
    rob = Robot()
    print(rob.reset())
