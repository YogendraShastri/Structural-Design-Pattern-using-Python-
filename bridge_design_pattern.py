# """ 
#                       [ implementation ]                                    [ Abstraction ]
#
#                             Device                                               Remote
#                 { PowerOn, PowerOff, set_channel}  --------------  { toggle_power, change_chennel}
#                        /             \                                      /               \ 
#                       /               \                                    /                 \ 
#                  TV(Device)           Radio(Device)                SmartRemote(Remote)     BasicRemote(Remote)
# """

from abc import ABC, abstractmethod

class Device(ABC):

    @abstractmethod
    def power_on(self):
        pass

    @abstractmethod
    def power_off(self):
        pass

    def change_channel(self, channel):
        pass

class TV(Device):

    def power_on(self):
        print("TV is Powering ON")

    def power_off(self):
        print("TV is powering OFF")

    def change_channel(self, channel):
        print(f"TV is set to channel : {channel}")

class Radio(Device):

    def power_on(self):
        print("Radio is powering on")
    
    def power_off(self):
        print("Radtio is powering off")

    def change_channel(self, channel):
        print(f"Radio channel set to {channel}")

#abstraction
class Remote(ABC):
    def __init__(self, device):
        self.device = device

    @abstractmethod
    def toggle_power(self, power):
        pass

    @abstractmethod
    def set_channel(self, channel):
        pass

class SmartRemote(Remote):

    def toggle_power(self, power):
        if power == "ON":
            return f"Smart Remote : {self.device.power_on()}"
        else:
            return f"Smart Remote : {self.device.power_off()}"
    
    def set_channel(self, channel):
        return f"SmartRemote : {self.device.change_channel(channel)}"
    
    def subscription(self):
        print("Use Hotstar, Sony liv  or Netflix")
    
class BasicRemote(Remote):

    def toggle_power(self, power):
        if power == "On":
            return f"Basic Remote : {self.device.power_on()}"
        else:
            return f"Basic Remote : {self.device.power_off()}"
    
    def set_channel(self, channel):
        return f"Basic Remote : {self.device.change_channel(channel)}"


if __name__ == "__main__":
    tv = TV()
    radio = Radio()

    tv_remote = SmartRemote(tv)
    radio_remote = BasicRemote(radio)
    
    tv_remote.toggle_power("ON")
    tv_remote.set_channel(23)
    tv_remote.subscription()
    tv_remote.toggle_power("OFF")

    print("\n")
    radio_remote.toggle_power("ON")
    radio_remote.set_channel(94.6)
    radio_remote.toggle_power("OFF")
