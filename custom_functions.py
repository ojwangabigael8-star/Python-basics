def greet():
    print("hello")

def greeting(name):
    print(f"Hello {name}")

# greeting('Abby')
# greeting('Frank')
# greeting('Bob')
# greeting('Faith')
# greet() # call == use no arguments/ params == data

def volume_cylinder(radius, height):
     v = 22/7 * radius**2 * height
     return v

# volume_cylinder(50, 50)
# volume_cylinder(35,21)
# volume_cylinder(7,14)

def volume_cylinder2(radius, height):
    v = 22/7 * radius**2 * height
    return v

result = volume_cylinder2 ( 7,14)
print(round(result))

def surface_area(radius, height):
    v = 22/7 * radius**2 * height
    a = 22/7 * radius**2 *2 + 22/7 * radius**2 * height
    return v, a

volume, area = surface_area( 7, 14)
print(f"volume is {volume}) and area is {area}")

#name
volume, area = surface_area(height=21, radius=7)
print(f"volume is {volume}) and area is {area}")

def divide(x, y, should_round=False):
    res= x / y
    if should_round:
        return round(res,2)
    else:
        return res


print(divide(8, 2,True))
print(divide(56,11,True))