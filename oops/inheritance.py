# python code to demonstrate how parent constructors
# are called

# parents class
class Person(object):
    #__init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("My id is {}".format(self.idnumber))


# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        # invoking the __init__of the parent class
        Person.__init__(self, name, idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("Idnumber: {}".format(self.idnumber))
        print("post: {}".format(self.post))

# creation of an object variables or an instance
a = Employee('Rahul', 685768572, 2000000, "Intern")

# calling a function of the class person using it instance
a.display()
a.details()

