class Dog:
    #class attribute
    attr1 = "mammal"
    #instacce attribute
    def __init__(self, name):
        self.name = name
# Driver code
# object instantiation

Rodger = Dog("Rodger")
Tommy = Dog("Tommy")
# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is a {}".format(Tommy.__class__.attr1))

# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))

class Dog:
    # class attribute
    attr1 = "mammal"
    # instance attribute
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("My name is {}".format(self.name))
# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")
# Accessing class methods
Rodger.speak()
Tommy.speak()