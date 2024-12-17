class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        if args in cls.houses_history:
            instance = super().__new__(cls)
            return instance
        else:
            cls.houses_history += args
            instance = super().__new__(cls)
            return instance

    def __init__(self, name, number_of_floors):
        self.name = name
        if isinstance(number_of_floors, int) and number_of_floors > 0:
            self.number_of_floors = number_of_floors
        else:
            raise ValueError('Этаж должен быть целым числом и больше 0.')

    def __del__(self):
        print(f" {self.name} снесён, но он останется в истории")

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)
