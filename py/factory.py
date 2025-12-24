class Pizza:
    def __init__(self, size):
        self.size = size

    def __str__(self):
        return f"{self.size} pizza"

class MargheritaPizza(Pizza):
    def __init__(self, size):
        super().__init__(size)
        self.toppings = ["Tomato", "Mozzarella", "Basil"]

    def __str__(self):
        return f"{self.size} Margherita with {', '.join(self.toppings)}"

class PepperoniPizza(Pizza):
    def __init__(self, size):
        super().__init__(size)
        self.toppings = ["Tomato", "Mozzarella", "Pepperoni"]

    def __str__(self):
        return f"{self.size} Pepperoni with {', '.join(self.toppings)}"


class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type, size):
        if pizza_type == "margherita":
            return MargheritaPizza(size)
        elif pizza_type == "pepperoni":
            return PepperoniPizza(size)
        else:
            raise ValueError("Unknown pizza type")

# Example usage:

pizza1 = PizzaFactory.create_pizza("margherita", "Medium")
pizza2 = PizzaFactory.create_pizza("pepperoni", "Large")

print(pizza1)
print(pizza2)
