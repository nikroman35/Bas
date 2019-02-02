import os
class aircrack:
    @staticmethod
    def monitor_mode():
        result = os.system("airodump-ng --write test wlan0mon")

