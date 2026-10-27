# store  many items
from dateutil.relativedelta import weekdays

from bmi import weight, height

ages = [21,43,45,77,95,16,18,92] #list

names = ["Abby","Jeff","Frank","Essy","Precious"]

#functions
ages.append(23)
#ages.clear()
#ages.sort()
#ages.reverse()
print(ages)

#names.sort()
#names.reverse()
# names.append("Claire")
# print(names)
#
# frank_count = names.count("Frank")
# print(frank_count)
#
# print(len(names))
# print(len(ages))
#
# print(sum(ages)/len(ages))
#
# # retrieve an element
# print(ages[3])
#
# print(names[4])
# print(names[-1])
#
# print(names[-4:]) # slicing
# print(names[::-1])
# print(ages[3:5])
#
# print(ages[::-1])

# set
scores = {88, 43, 32, 88, 76, 54} # no duplicates
print(scores)

#tuple immutable
weekdays=("Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun")
print(weekdays)
print(weekdays[0])
print(weekdays[1])
print(weekdays[2])

# dictionary
person = {"name": "Abby", "age": 20, "weight": 48, "height":1.5}
print(person["name"])
print(person["age"])
print(person["weight"])

people = [
         {"name": "Abby", "age": 20, "weight": 48 },
         {"name": "Jeff", "age": 23, "weight": 70 },
         {"name": "Frank", "age": 20, "weight": 65 },

         ]
print(people)


