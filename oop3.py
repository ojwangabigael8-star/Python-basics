# Back acc == owner, acc no, balance, history
from datetime import date, datetime


class Client:
    def __init__(self, name, kra_pin, dob, gender):
        self.name = name
        self.kra_pin = kra_pin
        self.dob = dob
        today = date.today()
        birth_date = datetime.strptime(dob,"%d-%m-%Y")
        age = today.year - birth_date.year


        self.gender = gender

    def print_details(self):
        print(self.name)
        print(self.kra_pin)
        print(self.dob)

    def calc_age(self):
        today = date.today()
        birth_date = datetime.strptime(self.dob,"%d-%m-%Y")
        age = today.year - birth_date.year
        return age

class BankAccount:
    def __init__(self, owner, acc_no, balance):
        self.owner = owner
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += abs(amount)  # -100

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money")
        else:
            self.balance -= abs(amount)

    def print_details(self):
        print(self.owner.name)
        print(self.acc_no)
        print(self.balance)
        print("------------")


Abby = Client('Abigael Ojwang', 'A0002', '10-09-2006', 'Female')
Frank = Client('Frank Abdii', 'A0005', '05-01-2006', 'Male')

acc1 = BankAccount(Abby, acc_no="42721138", balance=50000)
acc2 = BankAccount(Abby, acc_no="42746738", balance=70000)
acc3 = BankAccount(Frank, acc_no="01124546", balance=50000)

acc1.deposit(5000)
acc1.deposit(250)

acc1.print_details()
acc1.withdraw(5000)
acc1.print_details()

# dob = '10-09-2006'  # d.m.y d/m/y hh:mm:ss

# today = date.today()
# print(f"{today.day}/{today.month}/{today.year}")
# convert string to date
# birth_date = datetime.strptime(dob,"%d-%m-%Y")
# age = today.year - birth_date.year
# print(age)

print("Abby's Age", Abby.calc_age())
print("Frank's Age", Frank.calc_age())


# ctrl + alt + l =format
