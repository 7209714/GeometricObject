from CIrcle import Circle
from RectangleGEO import Rectangle

def main():

    a=int(input())
    b=int(input())
    v=int(input())
    c1=input()
    f1=input()
    c2=input()
    f2=input()  
    circle = Circle(a,c1,f1)    
    rectangle = Rectangle(b, v,c2,f2)
    
    print("Circle:")
    print("Radius is", circle.getRadius())
    print("Diameter is", circle.getDiameter())
    print("Area is ", circle.getArea())
    print("Perimeter is", circle.getPerimeter())
    circle.__str__()
    print("\n")
    print("Rectangle:")
    print("Width is", rectangle.getWidth())
    print("Height is", rectangle.getHeight())
    print("Area is", rectangle.getArea())
    print("Perimeter is", rectangle.getPerimeter())
    rectangle.__str__()
    
main() 

