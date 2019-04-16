
import netifaces
import subprocess
class config:

    @staticmethod

    def get_connected_network():
        info = netifaces.ifaddresses(config.get_actual_interface())
        addr = info[netifaces.AF_INET][0]['addr']
        addr_subnet = addr.split('.')[:-1]
        str_addr_subnet = '.'.join(addr_subnet) + '.1/24'
        return str_addr_subnet

    def get_actual_interface():
        state = netifaces.interfaces()
        interface_array = []
        for interface in state:
            if interface[0] == "w":
                interface_array.append(interface)
        return interface_array[0]

    def get_interface_name():
        result = subprocess.Popen('sudo iw dev',shell=True,stdout=subprocess.PIPE)
        out, err = result.communicate()
        print(out)
        a = str(out)
        b = a.find('0')
        print(b)