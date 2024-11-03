class Person:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    @property
    def Name(self,):
        return self.__name


    @Name.setter
    def Name(self, value):
        if value == "bob":
            self.__name = value
        else:
            self.__name = value
    @staticmethod
    def mymethod():
        print("Hello Word")

Person.mymethod()

p1 = Person("Mike", 20,"M")
print(p1.Name)





p1 = Person("Mike", 20, "M")
print(p1.Name)
print(p1.Name)


