#!/usr/bin/python
import os
from Classes.constants import constants
a = input("Enter command\n")
def swithUserCommand(string):
    return constants.userCommandDict[string]
b = swithUserCommand(a)
print(type(b))
