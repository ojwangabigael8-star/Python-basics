# class Student():# First define parent
#     def __init__(self, name, age):
#         self.name = name  # save name inside this object
#         self.age = age  # save age inside this object
#     def greet(self):
#         print(f"Hello,I am {self.name}")
#
# s1 = Student("Sarah", 25)
# s2 = Student("Michael", 30)
# print(s1.name)
# print(s1.age)
# print(s2.name)
# print(s2.age)
#
#
# s1 = Student("Sarah", 25)
# s1.greet()
#
# # university student gets everything from the student + more
#
# class UniversityStudent(Student):
#     def __init__(self, name, age, course):
#         super().__init__(name, age) #says :"Hey parent student ,do your __init__job"
#         self.course = course
#
#     def study(self):
#         print(f"{self.name} is studying {self.course}")
#
# u1=UniversityStudent("Michael", 30, "BBIT")
# u1.greet()
# u1.study()

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}.New: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}.New: {self.balance}")
        else:
            print("Insufficient funds")


acc = BankAccount("John", 10000)
acc.deposit(450)
acc.withdraw(750)


