import copy

class Car:
    def __init__(self):
        self.model=""
        self.make=""
    
    def clone(self):
        return copy.deepcopy(self)
    

# Example usage
car1 = Car()
car1.model = "Model S"
car1.make = "Tesla"

car2 = car1.clone()
print(car2.model)  # Output: Model S
print(car2.make)   # Output: Tesla

## Now if car2 is modified, car1 remains unchanged
car2.model = "Model 3"
print(car1.model)  # Output: Model S
print(car2.model)  # Output: Model 3

## And also verifing issue of deep copy
print(car1 is car2)  # Output: False