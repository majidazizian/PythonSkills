import random
import string


class Robot(object):

    alreadyRoboteNames = []
    name = ""

    def __init__(self):

        self.reset()
            

    def reset(self):
        nameFound = False
        while nameFound == False:
            newName = self.nameGenerator()
            if (newName in self.alreadyRoboteNames) == False:
                nameFound = True
                self.name = newName
                self.alreadyRoboteNames.append(newName)

    def nameGenerator(self):
        char = ''.join(random.choice(string.ascii_uppercase) for _ in range(2))
        digit = ''.join(random.choice(string.digits) for _ in range(3))

        return char + digit


