class Figure:
    sides_count = 0
    def __init__(self, __color, __sides):
        self.__sides = __sides
        self.__color = __color
        self.filled = None
        self.__check_sides()

    def get_color(self):
        return list(self.__color)

    def __is_valid_color(self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g , b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        count = 0
        for i in args:
            count += 1
        if count == self.sides_count:
            for value in args:
                if isinstance(value, int) and value > 0:
                    continue
                else:
                    return False
            return True
        else:
            return False

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = [*new_sides]
            return self.__sides

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.get_sides())

    def __check_sides(self):
        if self.__check_cube():
            return
        if isinstance(self.__sides, int):
            self.__sides = [self.__sides for _ in range(self.sides_count)]
            return
        elif len(self.__sides) == self.sides_count:
            self.__sides = list(self.__sides)
        elif len(self.__sides) > self.sides_count:
            self.__sides = [1 for _ in range(self.sides_count)]
        else:
            self.__sides = [1 for _ in range(self.sides_count)]

    def __check_cube(self):
        if self.sides_count == 12:
            if isinstance(self.__sides, int):
                self.__sides = [self.__sides for _ in range(self.sides_count)]
                return
            else:
                self.__sides = [1 for _ in range(self.sides_count)]




class Circle(Figure):
    sides_count = 1
    def __init__(self, __color, __sides):
        super().__init__(__color, __sides)
        self.__radius = self.get_radius()

    def get_radius(self):
        for i in self.get_sides():
            dlina_okr = i
            radius = i / (2 * 3.14)
            return radius

    def get_square(self):
        return 3.14 * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3
    def __init__(self, __color, __sides):
        super().__init__(__color, __sides)

    def get_square(self):
        p = (self.get_sides()[0] + self.get_sides()[1] + self.get_sides()[2]) / 2
        from math import sqrt
        s = sqrt(p * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2]))
        return s

class Cube(Figure):
    sides_count = 12
    def __init__(self, __color, __sides):
        super().__init__(__color, __sides)

    def get_volume(self):
        v = self.get_sides()[0] ** 3
        return v


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())