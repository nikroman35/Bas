import subprocess
import time
import os
import csv
from Classes.airodumpNet import airodumpNet

class aircrack:
    interface_mode = str
    @staticmethod
    def check_wlan_mode():
        cmd = os.listdir('/proc/net/dev_snmp6')
        lo = 'lo'
        eth0 = 'eth0'
        if lo in cmd:
            cmd.remove('lo')
        if eth0 in cmd:
            cmd.remove('eth0')
        result = subprocess.Popen("sudo iwconfig %s" % cmd[0],shell=True,stdout=subprocess.PIPE)
        out, err = result.communicate()
        interface_mode_index = str(out)
        mode_index = interface_mode_index.find('Mode:')
        interface_mode = interface_mode_index[(mode_index + 5): (mode_index + 8)]
        return interface_mode

    def monitor_mode():
        cmd = 'sudo airmon-ng start wlan0'
        subprocess.call(cmd, shell=True)

    def managed_mode():
        cmd = 'sudo airmon-ng stop wlan0mon'
        subprocess.call(cmd, shell=True)

    def airodump_call():
        cmd = 'sudo airodump-ng --write txt wlan0mon'
        result = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        time.sleep(5)
        result.kill()

    def sort_by_power(arr):
       return arr[8]

    def search_network():
        filename = 'txt-01.csv'
        with open(filename, 'r', newline = '') as file:
            file_reader = csv.reader(file)
            kek = [row for row in file_reader]
            kek.pop(1)
            network_mas = []
            for a in kek:
                if len(a) == 0:
                    continue
                if a[0] == 'Station MAC':
                    break
                network_mas.append(a)
            network_mas.sort(key = aircrack.sort_by_power,reverse = True)
            current_net = network_mas[0]
            a = airodumpNet(current_net[0],
                            current_net[3],
                            current_net[5],
                            current_net[8],
                            current_net[9],
                            current_net[10],
                            current_net[13])
            print(a.power)







