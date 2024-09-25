
class Animal:
    alive = True
    fed = False
    def __init__(self, name):
        self.name = name

class Plant:
    edible = False
    def __init__(self, name):
        self.name = name

class Fruit(Plant):
    edible = True
class Flower(Plant):
    edible = False
class Mammal(Animal):
    def eat(self,food):
        print(f'{self.name} съел {food.name}')
        Mammal.fed = True
class Predator(Animal):
    def eat(self,food):
        if Plant.edible == True:
            Predator.fed = True
            print(f'{self.name} съел {food.name}')
        else:
            Predator.alive = False
            print(f'{self.name} не съел {food.name}')

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
