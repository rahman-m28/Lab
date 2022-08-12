from pytest import *
from classes import *

class Test:
    def setup_method(self):
        self.tv1 = Television()
    
    def teardown_method(self):
        del self.tv1

    def test_get_tv_status(self):
        assert self.tv1.get_tv_status()==False
        self.tv1.power()
        assert self.tv1.get_tv_status()==True
        self.tv1.power()
        assert self.tv1.get_tv_status()==False
        assert self.tv1.get_tv_status()==False

    def test_get_channel(self) -> int:
        assert self.tv1.get_channel()==Television.MIN_CHANNEL
        
        self.tv1.channel_up()
        assert self.tv1.get_channel()==Television.MIN_CHANNEL

        self.tv1.power()
        self.tv1.channel_up()
        assert self.tv1.get_channel()==Television.MIN_CHANNEL+1

        self.tv1.power()
        assert self.tv1.get_channel()==Television.MIN_CHANNEL+1

        self.tv1.power()
        self.tv1.channel_down()
        assert self.tv1.get_channel()==Television.MIN_CHANNEL

        self.tv1.channel_down()
        assert self.tv1.get_channel()==Television.MAX_CHANNEL-1

        self.tv1.channel_up()
        assert self.tv1.get_channel()==Television.MIN_CHANNEL

    def test_get_volume(self):
        assert self.tv1.get_volume()==Television.MIN_VOLUME
        
        self.tv1.volume_up()
        assert self.tv1.get_volume()==Television.MIN_VOLUME

        self.tv1.power()
        self.tv1.volume_up()
        assert self.tv1.get_volume()==Television.MIN_VOLUME+1

        self.tv1.power()
        assert self.tv1.get_volume()==Television.MIN_VOLUME+1

        self.tv1.power()
        self.tv1.volume_down()
        assert self.tv1.get_volume()==Television.MIN_VOLUME

        self.tv1.volume_down()
        assert self.tv1.get_volume()==Television.MAX_VOLUME

        self.tv1.volume_up()
        assert self.tv1.get_volume()==Television.MIN_VOLUME
