class Pizza:

    def __init__(self):
        self.name = ""
        self.crust = ""
        self.toppings = ""
        self.size = ""

    def add_topping(self):
        self.toppings += (self)

    #def pizza_order(self):
    #    print()

order1 = Pizza()

print(dir(order1))