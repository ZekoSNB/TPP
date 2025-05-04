import psutil
import time
import os


# this class is used to process data of the procesor (temp, usage, etc)
class Data():
    def __init__(self):
        print(self.get_cpu_freq())

    def get_cpu_temp(self):
        return psutil.sensors_temperatures()['coretemp'][0].current

    def get_cpu_freq(self):
        return psutil.cpu_freq() 


