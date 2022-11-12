import time


class TrafficLight:
    __color = "красный"

    def running(self, color, duration):
        self.__color = color
        print(f"Цвет светофора - {self.__color}")
        time.sleep(duration % 1)
        for i in range(int(duration), 0, -1):
            print(i)
            time.sleep(1)
        print(0)


traffic_light = TrafficLight()
traffic_light.running("Красный", 7)
traffic_light.running("Оранжевый", 2)
traffic_light.running("Зелёный", 5)
