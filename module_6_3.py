

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed, cords = [0, 0, 0]):
        self.cords = cords
        self.speed = speed
    def move(self, dx, dy, dz):
        self.cords[0] += dx * self.speed
        self.cords[1] += dy * self.speed
        self.cords[2] += dz * self.speed
        self.check_z(dz)

    def check_z(self, dz):
        if self.cords[2] < 0:
            self.cords[2] -= dz * self.speed
            print("It's too deep, i can't dive :(")

    def get_cords(self):
        print(f'X: {self.cords[0]}, Y: {self.cords[1]}, Z: {self.cords[2]}')


    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print('Sorry, Im peaceful :)')
        else:
            print('Be, careful, Im attacking you 0_0')


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        import random
        print(f'Here are(is) {random.randint(1,4)} eggs for you')

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        self.cords[2] = int(self.cords[2] - (abs(dz) * (self.speed / 2)))


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    def __init__(self, speed,  sound = 'Click-click-click'):
        self.sound = sound
        super().__init__(speed)
    def speak(self):
        print(self.sound)


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()

print(db._DEGREE_OF_DANGER)