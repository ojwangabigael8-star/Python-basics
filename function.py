People= [
    {"name": "Abby", "age":23},
    {"name": "Job", "age":23},
    {"name": "Frank", "age":23},
]

# lambda x: x['age']
sorted_by_age = sorted(People, key= lambda x: x["age"], reverse=True)

print(sorted_by_age)

def addition(*nums):
    """
    Returns the sum of all the numbers passed as arguments
    parameters:
     integers or floats or a mix of integers and floats
    Returns:
     Integers or floats
    """