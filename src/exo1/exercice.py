class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Dami <3 !"


my_dog = Dog("Paul", 22)


class Circle:
    pi = 3.14159

    def __init__(self, raduis):
        self._radius = raduis

    @property
    def area(self):
        return Circle.pi * self._radius**2


circle = Circle(5)
print(circle.area)
