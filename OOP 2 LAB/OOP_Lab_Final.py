from abc import ABC, abstractmethod
class Product(ABC):
    def __init__(self, name, price=0.0,quantity_in_stock=0):
        self.name = name
        self._price = price
        self._quantity_in_stock = quantity_in_stock

    def get_price(self):
        return self._price
    def set_price(self,value):
        self._price=value
    
    def get_quantity_in_stock(self):
        return self._quantity_in_stock
    def set_quantity_in_stock(self,value):
        self._quantity_in_stock=value

    @abstractmethod
    def get_discount(self):
        pass

    def display(self):
        return f"Product: {self.name}, Price: Tk {self._price:.2f},Quantity in Stock: {self._quantity_in_stock}"


class Electronics(Product):
    def __init__(self,name,price,quantity_in_stock,seasonal_discount=0.3):
        super().__init__(name,price,quantity_in_stock)
        self.seasonal_discount=seasonal_discount

    def get_discount(self):
       return self.get_price()*self.seasonal_discount
    
    def display(self):
        discount_amount=self.get_discount()
        discounted_price= self.get_price() - discount_amount
        return f"{super().display()}, Discount Amount : Tk {discount_amount:.2f}, Discounted Price : Tk {discounted_price:.2f},"
    
class Clothing(Product):
    def __init__(self,name,price,quantity_in_stock,flat_discount=0.2):
        super().__init__(name,price,quantity_in_stock)
        self.flat_discount=flat_discount

    def get_discount(self):
        return self.get_price()*self.flat_discount

    def display(self):
        discount_amount=self.get_discount()
        discounted_price= self.get_price() - discount_amount
        return f"{super().display()}, Discount Amount : Tk {discount_amount:.2f}, Discounted Price : Tk {discounted_price:.2f},"
    

class Groceries(Product):
    def __init__(self,name,price,quantity_in_stock,purchase_quantity=0):
        super().__init__(name,price,quantity_in_stock)
        self.purchase_quantity = purchase_quantity

    def get_discount(self):
        if (self.purchase_quantity >= 5):
            return (self.get_price() *0.5)
            
        elif (self.purchase_quantity >= 3):
            return  (self.get_price() * 0.3)

    def display(self):
        discount_amount=self.get_discount()
        discounted_price= self.get_price() - discount_amount
        return f"{super().display()}, Discount Amount : Tk {discount_amount:.2f}, Discounted Price : Tk {discounted_price: .2f},"   

product_1=Electronics("Fridge",56000,2)
print(product_1.display())

product_2=Clothing("Shirt",1600,4)
print(product_2.display())

product_3=Groceries("Begun",78,10,5)
print(product_3.display())

