# Ken Leam G. Gamboa
# BSCPE 1-5
# This is an object-oriented program that tests particular functions of a TV.


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
        if self.activity.lower() == "on":
            print(self.name, "is on")
        else:
            print(self.name, "is off")
# create a method that will indicate the channel of Tv
# create a method that will set the channel of Tv
# create a method that will get the voulume level of the TV
# create a method that will set a new volume for the tv
# create a method that will increase the channel number by 1
# create a method that will decrease the channel number by 1
# create a method that will increase the volume level by 1
# create a method that will decrease the volume level by 1
# create two objects that satisfy the following arguments in the constructor
