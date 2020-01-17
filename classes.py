# Create a Pizza type for representing pizzas in Python. Think about some basic properties that would define a pizza's values; things like size, crust type, and toppings would help. Define those in the __init__ method so each instance can have its own specific values for those properties.

class Pizza:

    def __init__(self):
        self.crust = ""
        self.toppings = list()
        self.size = ""

# Add a method for interacting with a pizza's toppings, called add_topping.
    def add_topping(self, topping):
        self.toppings.append(topping)

# Add a method for outputting a description of the pizza (sample output below).

    def place_order(self):
        topping_string = ""
        for topping in self.toppings:
            topping_string += f"{topping}\n"
        print(f"I would like a {self.size}-inch, {self.crust} pizza with the following toppings:\n\n{topping_string}")


# Make two different instances of a pizza. If you have properly defined the class, you should be able to do something like the following code with your Pizza type.

meat_lovers = Pizza()
meat_lovers.size = 16
meat_lovers.crust = "deep dish"
meat_lovers.add_topping("pepperoni")
meat_lovers.add_topping("Italian sausage")
meat_lovers.add_topping("Canadian bacon")
meat_lovers.add_topping("bacon")
meat_lovers.place_order()

Hawaiian = Pizza()
Hawaiian.size = 14
Hawaiian.crust = "thin crust"
Hawaiian.add_topping("Canadian bacon")
Hawaiian.add_topping("pineapple")
Hawaiian.place_order()

# You should produce output in the terminal similiar to the following string.

# "I would like a 16-inch, deep-dish pizza with Pepperoni and Olives."