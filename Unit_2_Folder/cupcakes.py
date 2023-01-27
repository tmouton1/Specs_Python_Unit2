from abc import ABC, abstractmethod
import csv
from pprint import pprint

class Cupcake():
    size = "regular"
    def __init__(self, name, price, flavor, frosting, filling, sprinkles):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []
       


        # my_cupcake.frosting = "Chocolate"
        # my_cupcake.filling = "Chocolate"
        # my_cupcake.name = "Triple Chocolate"

    def add_sprinkles(self, *args):
            for sprinkle in args:
                self.sprinkles.append(sprinkle) 
    


    @abstractmethod
    def calculate_price(self, quantity):
        return quantity * self.price

my_cupcake = Cupcake(name='red velvet', price=5.00, flavor='chocolate', frosting='cream cheese',filling='vanilla', sprinkles='cinnamon')
                
my_cupcake.add_sprinkles('cinammon', 'powdered sugar')

print(my_cupcake.sprinkles)
# print(my_cupcake.price)
# print(my_cupcake.filling)

class Mini(Cupcake):
    size = "mini"
    def __init__(self, name, price, flavor,frosting,filling, sprinkles):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = sprinkles
 

    def calculate_price(self, quantity):
         return quantity * self.price

my_cupcake_mini = Mini(name='strawberry shortcake', price=3.00, flavor='strawberry', frosting='whipped cream',filling='strawberry jam', sprinkles='lemon')

print(my_cupcake_mini.filling)
print(my_cupcake_mini.frosting)
print(my_cupcake_mini.name)


class Jumbo(Cupcake):
    size = "extra large"
    def __init__(self, name, price, flavor,frosting,filling, sprinkles):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = sprinkles
      

    def calculate_price(self, quantity):
        return quantity * self.price
        
my_cupcake_jumbo = Jumbo(name='peanut butter swirl', price=7.00, flavor='peanut butter chocolate', frosting='chocolate',filling='peanut butter', sprinkles='resees')

print(my_cupcake_jumbo.frosting)
print(my_cupcake_jumbo.price)

class Duo(Cupcake):
    size = "two minis"
    def __init__(self, name, price, flavor,frosting,filling, sprinkles):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = sprinkles
        

    def calculate_price(self, quantity):
        return quantity * self.price

my_cupcake_duo = Duo(name='choco freeze', price=9.00, flavor='mint chocolate', frosting='chocolate',filling=' mint chip fudge', sprinkles='peppermint')

print(my_cupcake_duo.frosting)
print(my_cupcake_duo.sprinkles
)

with open("cupcakes.csv") as csvfile:
    reader = csv.DictReader (csvfile)

    for row in reader:
        print(row)

    for row in reader:
        pprint(row)

    cupcake1 = Cupcake('red velvet', 5.75, 'chocolate', 'cream cheese','vanilla','cinnamon')
    cupcake2 = Mini('strawberry shortcake', 3.75, 'strawberry', 'whipped cream','strawberry jam', 'lemon')
    cupcake3 = Jumbo('peanut butter swirl', 7.75, 'peanut butter chocolate','chocolate','peanut butter', 'resees')
    cupcake4 = Duo('choco freeze', 9.75, 'mint chocolate', 'chocolate',' mint chip fudge', 'peppermint')

    cupcake_list = [
        cupcake1,
        cupcake2,
        cupcake3,
        cupcake4
    ]
# 
#============================================================================================


def write_new_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()

        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({"size":cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
            else:
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcakes.sprinkles})
                
write_new_csv("cupcakes.csv", cupcake_list)

# ==============================================

def add_cupcake(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        if hasattr(cupcake, "filling"):
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
        else:
            writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})
        
        
def get_cupcakes(file):
    with open("cupcakes.csv") as csvfile:
        reader = csv.DictReader (csvfile)
        return list(reader)
    return reader

print(get_cupcakes(csvfile))


def find_cupcake(file,name):
    for cupcake in get_cupcakes(file):
        if cupcake ['name'] == name:
            return cupcake
        return None
        
def add_cupcake_dictionary(file, cupcake):
    with open(file, "a", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)

        


def read_csv(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)

    for row in reader:
        pprint(row)








                