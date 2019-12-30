import random
import string

class Robot(object):
    used_names = set()
    def __init__(self): 
        
        self.name = self.reset() 
    
    def reset(self):
        robot = Robot.generate_name()
        if robot not in Robot.used_names:
            Robot.used_names.add(robot)
            robot = Robot.generate_name()
        self.name = robot
        return self.name

    @classmethod
    def generate_name(cls):

        robot_name = ''
        for _ in range(2):
            letters =  random.choices(string.ascii_uppercase) # this generates list
            robot_name += letters[0]

        for _ in range(3):
            digits = random.choices(string.digits)  # this generates list
            robot_name += digits[0]
        return robot_name

if __name__ == '__main__':
    rob = Robot()
    # print(rob.generate_name())
    print(f"old name is {rob.generate_name()}, resetted: {rob.reset()}")
    print(rob.used_names)
