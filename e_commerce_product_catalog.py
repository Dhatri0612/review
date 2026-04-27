# Dhatri->Task 1 – E‑commerce Product Catalog
# Scenario
# Design an e‑commerce product catalog that supports multiple product types (e.g., Book, Electronics, Clothing) with different behavior and discount logic.
# OOP‑Covered
# Classes, objects, inheritance, polymorphism, abstraction, encapsulation
# Instructions
# Create an abstract base class Product with attributes like id, name, price and a method getFinalPrice().
# Create derived classes Book, Electronics, Clothing which implement getFinalPrice() with their own logic (e.g., books: 10% discount, electronics: 5% discount, clothing: no discount).
# In main:
# Create a list of Product objects with mixed types.
# Demonstrate polymorphism by calling getFinalPrice() on them without down‑casing.
# Add validation inside setters (e.g., price > 0).

from abc import ABC , abstractmethod
class Product(ABC):
    def __init__(self,id ,name,price):
        self.set_id(id)
        self.set_name(name)
        self.set_price(price)

    def set_id(self,id):
        if id<=0:
            raise ValueError("ID must be greater than 0")
        self.__id=id

    def set_name(self,name):
        if not name:
            raise ValueError("Name cannot be empty")
        self.__name=name

    def set_price(self,price):
        if price <=0:
            raise ValueError("Price must be greater than 0")
        self.__price=price

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price 
    
    @abstractmethod
    def getFinalPrice(self):
        pass

class Book(Product):
    def getFinalPrice(self):
        price=self.get_price()
        return price-(price*0.10)

class Electronics(Product):
    def getFinalPrice(self):
        price=self.get_price()
        return price-(price*0.05)

class Clothing(Product):
    def getFinalPrice(self):
        return self.get_price()
    
products=[Book(1,"Python Book",800),Electronics(2,"Earbuds",2000),Clothing(3,"Shirt",500)]

for product in products:
    print(f"Product ID: {product.get_id()}")
    print(f"Product: {product.get_name()}")
    print(f"Final Price: {product.getFinalPrice()}")
    print()
