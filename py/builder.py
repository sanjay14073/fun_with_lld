'''
This file is for illustrating the builder pattern
So why the builder pattern ?
It is essential when we want flexibility lets consider a simple example
when we want to contruct an house different people would have different requirements to address this we
require a system design pattern this is a pattern that can accomplish that.
'''

class House:
    def __init__(self, floors, color, modular_kitchen, interior_design):
        self.floors = floors
        self.color = color
        self.modular_kitchen = modular_kitchen
        self.interior_design = interior_design

    def __str__(self):
        return f"{self.floors} {self.color} {self.modular_kitchen} {self.interior_design}"


class HouseBuilder:
    def __init__(self):
        self._floors = 1
        self._color = "White"
        self._modular_kitchen = False
        self._interior_design = False

    def add_floors(self, floors):
        self._floors = floors
        return self

    def add_color(self, color):
        self._color = color
        return self

    def add_modular_kitchen(self):
        self._modular_kitchen = True
        return self

    def add_interior_design(self):
        self._interior_design = True
        return self

    def build(self):
        return House(
            self._floors,
            self._color,
            self._modular_kitchen,
            self._interior_design
        )


## Now customer 1 comes he wants color as blue and want 2 floors and all facilites 
# and customer 2 only wants 1 floor and no facitiy this is how simple it becomes to add things

house1 = (
    HouseBuilder()
    .add_color("Blue")
    .add_floors(2)
    .add_modular_kitchen()
    .add_interior_design()
    .build()
)

house2 = HouseBuilder().build()

print(house1)
print(house2)

