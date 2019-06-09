from GeometricObject import GeometricObject
import math 

class Circle(GeometricObject):
    
    def __init__(self,radius,color,filled):
        self.__radius = radius  
        self.setColor(color)
        self.setFilled(filled)
        self.__radius = radius  
    def setRadius(self, radius):
        self.__radius = radius         
    def getRadius(self):
        return self.__radius
    def getArea(self):
        return self.__radius*self.__radius*math.pi
    def getPerimeter(self):
        return self.__radius*2*math.pi
    def getDiameter(self):
        return self.__radius*2



