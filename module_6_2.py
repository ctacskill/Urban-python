class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.model = __model
        self.engine_power = __engine_power
        self.color = __color
    def get_model(self):
        return f'Модель: {self.model}'
    def get_horse_power(self):
        return f'Мощность двигателя: {self.engine_power}'
    def get_color(self):
        return f'Цвет: {self.color}'
    def print_info(self):
        print(Vehicle.get_model(self))
        print(Vehicle.get_horse_power(self))
        print(Vehicle.get_color(self))
        print(self.owner)
    def set_color(self, new_color):
        if new_color.lower() in Vehicle.__COLOR_VARIANTS:
            self.color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()