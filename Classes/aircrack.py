import subprocess
import time
import os
import signal
class aircrack:
    @staticmethod
    def monitor_mode():
        cmd = 'sudo airodump-ng --write txt wlan0mon'
        result = subprocess.Popen(cmd,shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
        time.sleep(10)
        result.kill()

