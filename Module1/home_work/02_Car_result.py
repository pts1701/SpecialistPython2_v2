# Сюда отправляем решение задачи "Автомобиль"
# Само задание в файле 02_Сar_task.md

class Car:
    def __init__(self, gas, tank, consum, odo):
        self.gas = gas #50l
        self.tank = tank #100l
        self.consum = consum #10l/100km
        self.odo = odo

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
            route = range
            self.gas = 0
        else:
            self.gas = self.gas - route * self.consum / 100
        self.odo = self.odo + route
        print('you rode', route, 'km')

car1 = Car(50, 55, 10, 0)
car1.fill(10)
car1.car_ride(100)

print(car1.gas)
print(car1.odo)
