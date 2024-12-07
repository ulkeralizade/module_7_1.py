from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        file = open(self.__file_name, 'a')
        file.close()

    def get_products(self):
        file = open(self.__file_name, 'r')
        pprint(file.read())
        file.close()

    def add(self, *products):
        existing_products = set()
        file = open(self.__file_name, 'r')
        for line in file:
            product_name = line.strip().split(', ')[0]
            existing_products.add(product_name)
        file.close()

        file = open(self.__file_name, 'a')
        for product in products:
            if product.name in existing_products:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                file.write(str(product) + '\n')
                existing_products.add(product.name)
        file.close()

s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

s1.get_products()
