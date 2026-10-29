# oop2

class Circle:
    def __init__(self, radius):# setup
        self.radius = radius

    def area(self):
        return 22/7 *self.radius**2

    def perimeter(self):
        return 22/7 *self.radius* 2

    def print_details(self):
        print("Radius is ", self.radius)
        print("Area is ", self.area())
        print("Perimeter is ", self.perimeter())

c1 = Circle(14)
c2 = Circle(42)
c3 = Circle(35)

print(c1.area())
c1.print_details()

# branches -- cop -- master main