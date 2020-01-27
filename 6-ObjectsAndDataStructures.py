class Vehicle:

    def getFuelTankCapacityInLitters():
        pass

    def getLittersOfGasoline():
        pass

#vs

class Vehicle:

    def getPercentFuelRemaining():
        pass

#====================================================

class Square:
    def __init__(self, topLeft, side):
        self.topLeft = topLeft
        self.side = side

class Rectangle:
    def __init__(self, topLeft, height, width):
        self.topLeft = topLeft
        self.height = height
        self.width = width

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

class Geometry:
    def __init__(self):
        self.pi = 3.14

    def area(self,shape):
        if shape isinstance(Square):
            return shape.side * shape.side
        elif shape isinstance(Rectangle):
            return shape.width * shape.height
        elif shape isinstance(Circle):
            return self.pi * shape.radius * shape.radius

#====================================================

class Square:
    def __init__(self, topLeft, side):
        self.topLeft = topLeft
        self.side = side

    def area(self):
        return self.side * self.side

class Rectangle:
    def __init__(self, topLeft, height, width):
        self.topLeft = topLeft
        self.height = height
        self.width = width

    def area(self):
        return self.width * self.height

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
        self.pi = 3.14

    def area(self):
        return self.pi * self.radius * self.radius
    
