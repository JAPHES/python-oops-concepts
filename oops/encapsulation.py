# python program to
# demonstrate private members
# "_" double underscore represents private attribute
# private attributes start with "_"

# creating a derived class
class Base:
    def __init__(self):
        self.a = "Geeks forGeeks"
        self.__c = "Geeks forGeeks"

# creating a derived class
class Derived(Base):
    def __init__(self):

        # calling constructor of
        #base class
        Base.__init__(self)
        print("Calling private member of base class:")
        print(self.__c)

# Driver code
obj = Base()
print(obj.a)



