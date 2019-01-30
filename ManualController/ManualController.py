import os
from Classes.constants import constants
class ManualController:
    def swithUserCommand(string):
        return constants.userCommandDict[0]()
    def run(self):
        switch = input("Enter command\n")
        self.swithUserCommand(switch)
