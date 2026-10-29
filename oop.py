#oop
#object --> laptop ->
#name --> props
# classes

class Person:
    #constructor
    def __init__(self, name, dob,color, weight,height):
        self.name = name
        self.dob = dob
        self.color = color
        self.weight = weight
        self.height = height
    def display(self):
        print(f"Name is {self.name} and dob is {self.dob}")

    def get_bmi(self):
        result = self.weight / (self.height * self.height)
        return round(result, 2)

    # blueprint for creating objects

p1 = Person("Abby Kyle", "10-09-2006", "Black", 48.2, 1.85)
p2 = Person("Frank Abdii", "05-01-2005", "Black", 58.1, 1.67)

p1.display()
p2.display()

print(f"{p1.name} bmi is {p1.get_bmi()}") #ctrl + D
print(f"{p2.name} bmi is {p2.get_bmi()}") #ctrl + D