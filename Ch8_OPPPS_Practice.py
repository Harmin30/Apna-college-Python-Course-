# ...........Lets Practice OOPPS...........`
# 
#Q1 . Create student class that takes name and marks of 3 subjets as arguements in constructor
#    Then create a method to print the average.

class Student:
    def __init__(self,name,marks1,marks2,marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
        print("Adding new student in database")
    def average(self):
        avg = (self.marks1 + self.marks2 + self.marks3) / 3
        print(f"Average marks of {self.name} is: {avg:.2f}")
# Creating an object of class Student with parameters
s1 = Student("Karan", 85, 90, 78)
# Accessing the average method of the object s1
s1.average()  # Output: Average marks of Karan is: 84.33
# Creating another object of class Student with different parameters
s2 = Student("John", 92, 88, 95)
s2.average()  # Output: Average marks of John is: 91.67


#Q2. Crete account class with 2 attributes - account number and balance.
#    Create methods for debit, credit and printing the balance.

class Account:
    def __init__(self,acc,bal):
        self.account_no = acc
        self.balance = bal

    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Rs.",amount, "was debited successful. New balance is:", self.balance)
        else:
            print("Insufficient balance for debit operation.")

    def credit(self, amount):
        self.balance += amount
        print("Rs.",amount,"was Credited successful. New balance is:", self.balance)

    def print_balance(self):
        print(f"Account Number: {self.account_no}, Balance: {self.balance}")

acc1 = Account(12345, 10000)
print("User account Number",acc1.account_no)  
acc1.debit(1000)
acc1.credit(500)
acc1.credit(25000)
acc1.print_balance()  # Output: Account Number: 12345, Balance: 9500
 