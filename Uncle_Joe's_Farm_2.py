class Animals:
    def __init__(self, name=' ', weight=0, voice=' '):
        self.name = name
        self.weight = weight
        self.voice = voice


class Goose(Animals):
    pass


class Cow(Animals):
    pass


class Sheep(Animals):
    pass


class Chicken(Animals):
    pass


class Goat(Animals):
    pass


class Duck(Animals):
    pass


class Eggs(Goose, Chicken, Duck):
    def collect_eggs(self):
        for i in list_of_eggs:
            print(
                f'Мое призвание - это собирать яйца у существа с именем "{i.name}", весом в {i.weight} усл. ед., говорящего "{i.voice}".')


list_of_eggs = [ # list_of_eggs - это атрибут. Проще понимается если это записать так: list_of_eggs = Eggs("Гусь Серый", 50, "Га-Га-Га") -тут 3 аргумента потому, что это задано в параметрах на стр. 2. Просто в данном случае атрибут - это список со ножеством знаений.
    Eggs("Гусь Серый", 50, "Га-Га-Га"),
    Eggs("Гусь Белый", 45, "Га-Га-Га"),
    Eggs("Курица Ко-Ко", 47, "Кукареку"),
    Eggs("Курица Кукареку", 43, "Кукареку"),
    Eggs("Утка Кряква", 49, "Кря"),
]
Eggs.collect_eggs(list_of_eggs) # метод вызываем напрямую от класса и в него, соответственно помещаем нужный нам, в данном случае единственный, атрибут)


class Milk(Cow, Goat):
    def get_milk(self):
        for i in list_of_milk:
            print(
                f'Мое призвание - это доить существо с именем "{i.name}", весом в {i.weight} усл. ед., говорящую "{i.voice}".')


list_of_milk = [
    Milk("Корова Манькa", 33, "Му-Му"),
    Milk("Коза №1", 36, "Мееееееее"),
    Milk("Коза №2", 32, "Мееееееее")
]
Milk.get_milk(list_of_milk)


class Cut(Sheep):
    def make_cut(self):
        for i in list_of_cut:
            print(
                f'Мое призвание - это стричь существо с именем "{i.name}", весом в {i.weight} усл. ед., говорящее "{i.voice}".')


list_of_cut = [
    Cut("Овца №1", 77, "Беееее"),
    Cut("Овца №2", 73, "Беееее")
]
Cut.make_cut(list_of_cut)
