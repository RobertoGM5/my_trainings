class Item:
    #validating data type
    def __init__(self, name, price, quantity =10):
        print(f'an instance created : {name}')
        self.name = name
        self.price = price
        self.quantity = quantity
    #class method
    def calculate_total_price(self):
        return self.price * self.quantity

#creating instances/object of the class
item1 = Item('Phone',100,)# is equal to random_str = str('4')

# 2nd instance / Object
item2 = Item('Laptop', 1000)
print(item1.name,item1.price, item1.quantity)
print(item2.name, item2.price, item2.quantity)

print(item1.calculate_total_price())
item2.calculate_total_price()