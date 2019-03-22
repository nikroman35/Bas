from  Classes.aircrack import aireplay
from Classes.aircrack import aircrack
from Classes.nmap import Nmap

class constants:
    userCommandDict = [aircrack.check_wlan_mode,
                       aircrack.monitor_mode,
                       aircrack.managed_mode,
                       aircrack.airodump_call,
                       aircrack.search_network,
                       aircrack.search_station,
                       aircrack.aireplay_attack]
                       #Nmap.define_open_ports]
    intencity = {1: 'fast',
                 2: 'faster',
                 3: 'flood'}