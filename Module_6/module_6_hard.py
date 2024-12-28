class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color)
        self.filled = True
        self.__sides = list(sides) if len(sides) == self.sides_count else [1]

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(elem, int) and 0 <= elem <= 255 for elem in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        return all(isinstance(side, (int, float)) for side in sides) and len(sides) == self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides, ):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * 3.14)

    def get_square(self):
        return self.__radius ** 2 * 3.14


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        p = self.__len__() / 2
        return (p * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2])) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        side = sides[0] if len(sides) == 1 else [1]
        super().__init__(color, *(side,) * self.sides_count)

    def get_volume(self):
        return self.get_sides()[0] ** 3


if __name__ == "__main__":
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())

    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())

    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())

    # Проверка сторон треугольника:
    triangle1 = Triangle((120, 130, 140), 3, 4, 5)
    print(triangle1.get_sides())
    print(triangle1.get_square())

    # Проверка сторон и площади круга:
    circle2 = Circle((0, 0, 0), 31.4)
    print(circle2.get_sides())
    print(circle2.get_square())
