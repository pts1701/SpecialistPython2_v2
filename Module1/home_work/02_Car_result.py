# Сюда отправляем решение задачи "Автомобиль"
# Само задание в файле 02_Сar_task.md

class Car:
    def __init__(self, gas, tank, consum):
        self.gas = gas #50l
        self.tank = tank #100l
        self.consum = consum #10l/100km

    def fill(self, fill):
        if self.gas < self.tank:
            gas_in_tank = self.gas + fill
            if gas_in_tank > self.tank:
                overflow = gas_in_tank - self.tank
                print("To much gasoline, overflow = ", overflow)
            else:
                overflow = 0
            self.gas = self.gas + (fill - overflow)
        else:
            print('Tank is full no need for refill')

    def car_ride(self, route):
        range = self.gas / self.consum * 100
        if route >= range:
            print('you rode', range, 'km')
            self.gas = 0
        else:
            print('you rode', route, 'km')
            self.gas = self.gas - route * self.consum / 100


car1 = Car(50, 55, 7)
car1.fill(10)
car1.car_ride(500)

print(car1.gas)
