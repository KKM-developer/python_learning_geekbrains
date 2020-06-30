import time
class TrafficLight:
    __color = ['красный', 'желтый', 'зеленый']
    def running(self):
        print(self.__color[0])
        time.sleep(7)
        print(self.__color[1])
        time.sleep(2)
        print(self.__color[2])
        time.sleep(7)


some_ex = TrafficLight()

some_ex.running()
