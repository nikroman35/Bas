import nmap
import os

class nmap_object:
    ports = []
    def __init__(self, name):
        self.name = name

class Nmap:

    @staticmethod
    def test_nmap():
        nm = nmap.PortScanner()
        nm.scan('192.168.0.1/24')
        self_ip = Nmap.get_self_addr()
        print(nm.all_hosts())
        for host in nm.all_hosts():
            if host != self_ip:
                proto = nm[host].all_protocols()
                if 'tcp' in proto:
                    lport = nm[host]['tcp'].keys()
                    for port in lport:
                        print(nm[host]['tcp'][port]['state'])
        print("ALL HOST")

    def define_open_ports():
        nm = nmap.PortScanner()
        nm.scan('192.168.0.1/24')
        self_ip = Nmap.get_self_addr()
        nmap_arr = []
        for host in nm.all_hosts():
            print(host)
            proto = nm[host].all_protocols()
            if host != self_ip and 'tcp' in proto:
                nmap_o = nmap_object(host)
                lport = nm[host]['tcp'].keys()
                for port in lport:
                    if  nm[host]['tcp'][port]['state'] == 'open':
                        nmap_o.ports.append(port)
                print(nmap_o.name, nmap_o.ports)
                nmap_arr.append(nmap_o)

        return nmap_arr

    def get_self_addr():
        ipv4 = os.popen('ip addr show wlan0').read().split("inet ")[1].split("/")[0]
        return ipv4
