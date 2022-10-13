import math

Given_Definer = input("Radius or Diameter: ").capitalize()

class Circle_Radius():
    def __init__(self,radius):
        self.radius = radius
    def Area_With_Radius(self):
        return math.pi*(self.radius**2)
    def display(self):
        print("The area of the circle is", round(self.Area_With_Radius(), 2))

class Circle_Diameter():
    def __init__(self,diameter):
        self.diameter = diameter
    def Area_With_Diameter(self):
        return (math.pi*(self.diameter**2))/4
    def display(self):
        print("The area of the circle is", round(self.Area_With_Diameter(), 2))

if Given_Definer == "Radius":
    Rad = Circle_Radius(float(input("Radius: ")))
    Rad.display()

else:
    if Given_Definer == "Diameter":
        Dia = Circle_Diameter(float(input("Diameter: ")))
        Dia.display()

    else:
       if Given_Definer != "Diameter" and Given_Definer != "Radius":
            print("Error")




