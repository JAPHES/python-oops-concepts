# class

class car:
    # database table
    def __init__(self, make, model, year, color, speed):
        # tie the attributes to the current object
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.speed = speed
    # methods
    def print_name(self):
        print(f"This is the {self.make} {self.model}")

    def get_speed(self, distance):
        print(f"This is the speed of the {self.make} {self.model} {self.speed} {distance}")

## create objects
car1 = car("Toyota", "camry","2021","Black","240")
car2 = car("Toyota","Corolla", "2010","silver","120")

# create objecs
car1.print_name()
car2.print_name()
car2.get_speed("km/hr")


