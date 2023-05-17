# Ken Leam G. Gamboa
# BSCPE 1-5
# This is an object-oriented program that tests particular functions of a TV.

import time
# create a class named "TV"
class TV:
    # create a constructor to initialize the objects
    def __init__(self, name, activity, channel, volume):
        self.name = name
        self.activity = activity
        self.channel = channel
        self.volume = volume
    # create a method that will indicate if the TV is on/off
    def show_activity(self):
        #since it's stated that the activity should be on boolean:
        if self.activity:
            time.sleep(1)
            print(self.name, "is on\n")
        else:
            print(self.name, "is off\n")
    # create a method that will indicate the channel of Tv
    def show_channel(self):
        time.sleep(1)
        print(self.name, "is set on channel", self.channel, "\n")
    # create a method that will set a new channel number for the TV
    def set_channel(self, new_channel):
        self.channel = new_channel
    # create a method that will get the voulume level of the TV
    def show_volume(self):
        time.sleep(1)
        print(self.name, "is set on volume level", self.volume, "\n")
    # create a method that will set a new volume for the tv
    def set_volume(self, new_volume):
        self.volume = new_volume
    # create a method that will increase the channel number by 1
    def channel_up(self):
        self.channel += 1
        if self.channel > 120:
            self.channel = 1
        else:
            return
    # create a method that will decrease the channel number by 1
    def channel_down(self):
        self.channel -= 1
        if self.channel < 1:
            self.channel = 120
        else:
            return
    # create a method that will increase the volume level by 1
    def volume_up(self):
        self.volume += 1
        if self.volume > 7:
            self.volume = 7
        else:
            return
# create a method that will decrease the volume level by 1
    def volume_down(self):
        self.volume -= 1
        if self.volume < 0:
            self.volume = 0
        else:
            return
# create a method that will indicatee the status of the television
    def indicate_status(self):
        time.sleep(1)
        print(self.name + "'s set at channel", self.channel, "and has volume level", self.volume, "\n")
