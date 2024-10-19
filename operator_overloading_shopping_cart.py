class Order:
    def __init__(self):
        self.cart = []

    def add_to_cart(self , item):
        self.cart.append(item)
    
    def remove_from_cart(self, item):
        self.cart.remove(item)
    
    def __len__(self):
        return len(self.cart)
    
    def __str__(self):
        return str([item for item in self.cart])

a = Order()

a.add_to_cart("Banana")
a.add_to_cart("Apple")
a.add_to_cart("Pineapple")
a.add_to_cart("Brush")
a.add_to_cart("Ice")

a.remove_from_cart("Pineapple")
print(a)
print(len(a))