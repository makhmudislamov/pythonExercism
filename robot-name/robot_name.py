import random
import string
"""
Didn't quite understand what other methods should I have and what they should do. Currently it generates random names. 
I'll revisit
"""
class Robot(object):
    def __init__(self):  
        pass

    def name(self, seed = string.ascii_letters):

        robot_name = ''
        for _ in range(2):
            letters =  random.choices(seed) # this generates list
            robot_name += letters[0].upper()

        for _ in range(3):
            digits = random.choices(string.digits)  # this generates list
            robot_name += digits[0]
        return robot_name

    # def reset(self):
    #     return self.name(self)



if __name__ == '__main__':
    rob = Robot()
    print(rob.name())
    # print(rob.reset())
