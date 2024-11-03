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
    def __eq__(self, other):
        if isinstance(other, House) or isinstance(other, int):
            return self.floor == other.floor
    def __add__(self, value):
        self.floor += value
        return self
    def __radd__(self, value):
        return self.__add__(value)
    def __iadd__(self, value):
        return self.__add__(value)
    def __gt__(self, other):
        if isinstance(other, House) or isinstance(other, int):
            return self.floor > other.floor
    def __lt__(self, other):
        if isinstance(other, House) or isinstance(other, int):
            return self.floor < other.floor
    def __ge__(self, other):
        if isinstance(other, House) or isinstance(other, int):
            return self.floor >= other.floor
    def __le__(self, other):
        if isinstance(other, House) or isinstance(other, int):
            return self.floor <= other.floor
    def __ne__(self, other):
        if isinstance(other, House) or isinstance(other, int):
            return self.floor != other.floor


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

#__eq__
print(h1 == h2)

#__add__
h1 + 10
print(h1)
print(h1 == h1)

#__iadd__
h1 += 10
print(h1)

# __radd__
h2 = 10 + h2
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__