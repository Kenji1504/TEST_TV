# from test_tv.py, import class TV
from tv_object import TV

# create two objects that satisfy the following arguments in the constructor
tv_1 = TV("television 1", True, 118, 5)
tv_2 = TV("television 2", True, 2, 3)

tv_1.show_activity()
tv_1.indicate_status()
tv_1.set_channel(30)
tv_1.show_channel()
tv_1.set_volume(3)
tv_1.show_volume()
tv_1.indicate_status()

tv_2.show_activity()
tv_2.indicate_status()
tv_2.channel_up()
tv_2.show_channel()
tv_2.volume_down()
tv_2.show_volume()
tv_2.indicate_status()
