class House:
    def __init__(self, name, floor):
        self.name = name
        self.floor = floor
        str(self)

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if self.new_floor > self.floor:
            print('Такого этажа не существует')
        else:
            for i in range(self.new_floor):
                print(i + 1)

    def __len__(self):
        return self.floor

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.floor}'


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
h3 = House('ЖК Эльбрус', 10)
h4 = House('ЖК Акация', 20)

# __str__
print(h3)
print(h4)

# __len__
print(len(h3))
print(len(h4))