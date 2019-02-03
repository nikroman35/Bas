import os
from Classes.constants import constants
class ManualController:
    def switch_user_command(string):
        key = int(string)
        return constants.userCommandDict[key]()

    def run(self):
        switch = input("Enter command\n")
        self.switch_user_command(switch)
