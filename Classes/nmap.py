import nmap
import os

class nmap_object:
    ports = []
    def __init__(self, name):
        self.name = name

class Nmap:

    @staticmethod

    def define_open_ports():
        nm = nmap.PortScanner()
        nm.scan('192.168.0.1/24')
        self_ip = Nmap.get_self_addr()
        nmap_arr = []
        for host in nm.all_hosts():
            if host != self_ip:
                nmap_o = nmap_object(host)
                for proto in nm[host].all_protocols():
                    lport = nm[host][proto].keys()
                    for port in lport:
                        if  nm[host][proto][port]['state'] == 'open':
                            nmap_o.ports.append(port)
                    print(nmap_o.name, nmap_o.ports)
                    nmap_arr.append(nmap_o)

        #print(len(nmap_arr))
        #print(nmap_arr[0].ports, nmap_arr[0].name)
        #print(nmap_arr[1].ports, nmap_arr[1].name)
        return nmap_arr

    def get_self_addr():
        ipv4 = os.popen('ip addr show wlan0').read().split("inet ")[1].split("/")[0]
        return ipv4
