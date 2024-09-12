class Item():
    pay_rate = 0.8

    def __init__(self, name: str, cost: float, quantity=0) -> None:
        # Run validations to the recieved arguments
        assert cost >= 0, f"Cost is {cost} which is less than zero!"
        assert quantity >= 0, f"Quantity is {quantity} which is less than zero!"

        # Assign to self object
        self.name = name
        self.cost = cost
        self.quantity = quantity

    def calculate_total_cost(self):
        return self.cost * self.quantity * Item.pay_rate
    
item_1 = Item('Camera', -2, 2)
item_1.name = 'Phone'
item_1.cost = 100
item_1.quantity = 3


print(Item.__dict__)
print(item_1.__dict__)
print(item_1.cost)
