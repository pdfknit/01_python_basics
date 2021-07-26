import time


class TrafficLight:
    def __init__(self):
        self.__color = 'Red'

    def running(self):
        while True:
            self.__color = 'Red'
            print(f"\033[31m {self.__color}")
            time.sleep(7)
            self.__color = 'Yellow'
            print(f"\033[33m {self.__color}")
            time.sleep(2)
            self.__color = 'Green'
            print(f"\033[32m {self.__color}")
            time.sleep(5)


traffic_light = TrafficLight()
traffic_light.running()
