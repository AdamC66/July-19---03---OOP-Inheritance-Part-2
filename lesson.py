class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
        self.tax = 0.1
    
    def total(self):
        return self.price * (1+self.tax)

class Book(Product):
    def __init__(self,name,price):
        super().__init__(name,price)
        self.tax = 0


cart = [
 Product('Mobile Phone', 100),
 Product('Bicycle', 150),
 Book('Catcher In The Rye', 10),
 Book('The Martian', 15),
 Book('1984', 8)
]

print("Cart total:")
for item in cart:
    print(item.name,f'- ${item.total()}')
print("Total:", sum(item.total() for item in cart))

















# class Dog:
#     def __init__(self,name):
#         self.name = name

#     def make_noise(self):
#         print("Bark!")

#     def eat(self):
#         print(f'{self.name} eats a normal amount')
# class Greyhound(Dog):
#     def eat(self):
#        print(f'{self.name} eats a lot')   

# class Husky(Dog):
#     pass

# class Poodle(Dog):
#     def make_noise(self):
#         print("yip")


# dog1 = Greyhound("Santa's Little Helper")
# print(dog1.name)
# dog1.make_noise()
# dog1.eat()
# dog2 = Husky("Koda")
# print(dog2.name)
# dog2.make_noise()
# dog2.eat()