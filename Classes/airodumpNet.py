class airodumpNet:

    def __init__(self, BSSID, channel, privacy, power, beacons, IV, EESID):
        self.BSSID = BSSID
        self.channel = channel
        self.privacy = privacy
        self.power = power
        self.beacons = beacons
        self.IV = IV
        self.EESID = EESID

class airodumpStation:

    def __init__(self, MAC, power, packets, BSSID):
        self.BSSID = BSSID
        self.MAC = MAC
        self.power = power
        self.packets = packets
