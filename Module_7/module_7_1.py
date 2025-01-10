from pprint import pprint

class Product:
    def __init__(self, name: str, weigh: float, category: str):
        self.name = name
        self.weigh = weigh
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weigh}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name, 'r', encoding="utf-8") as file:
            return file.read().strip()



    def add(self, *products):
        have_products = self.get_products().split("\n")
        have_names = set()
        for line in have_products:
            if line:
                pr_name = line.split(', ')[0]
                have_names.add(pr_name)

        with open(self.__file_name, 'a', encoding="utf-8") as file:
            for product in products:
                if product.name in have_names:
                    print(f'Продукт {product.name} уже есть в магазине' )
                else:
                    file.write(str(product) + '\n')
                    have_names.add(product.name)



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__
s1.add(p1, p2, p3)

print(s1.get_products())

