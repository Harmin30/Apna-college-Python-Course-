#OOPS in Python
# Object-Oriented Programming (OOP) in Python
#To map with real word scenarios ,we started  using objects in code.

# Using functions redundacy is reduced and code is more readable.

# Class and object in python 

#Class is a blueprint for creating objects.

#creating class
class Student:
    name = "Harmin"

#creating object(instance) of class Student

s1 = Student()  # s1 is an object of class student
print(s1.name)  # Accessing the attribute 'name' of the object s1

#Constructor in Python
# A constructor is a special method that is automatically called when an object of a class is created.
# It is used to initialize the attributes of the class.
class Student:
#Default constructor: No arguments

    def __init__(self):
        pass

#Parameterized constructor: Takes arguments to initialize attributes

    def __init__(self,fullname,marks): #The self parameter refers to the instance of the class.
        self.name = fullname
        self.marks = marks
        print("adding new student in database")

s1 = Student("karan", 89)  # Creating an object of class Student with parameters
print(s1.name,s1.marks)  # Accessing the attribute 'name' of the object s1

s2 = Student("John", 95)  # Creating another object of class Student with different parameters
print(s2.name,s2.marks)  # Accessing the attribute 'name' of the object s2


#.....................Attributes in Python.....................


#Attrributes are variables that belong to the class and are used to store data related to the class.

#Attribues = Any data

# TWO types of attributes in python:

# 1. class attributes: Shared by all instances of the class. 
# 2. instance attributes: Unique to each instance of the class.

class Student:
    college = "ABC University"  # Class attribute
    name = "Harmin"  # class attribute

    def __init__(self,name,marks):
        self.name = name #obj attribute > class attribute 
        self.mark = marks
        print("adding new student in database")

s1 = Student("Prachi",98)
print(s1.name, s1.mark)  # Accessing instance attributes

#....Note : When class attribute and instance attribute have the same name,
#           the instance attribute takes precedence over the class attribute.


#............Methods in Python.................

# Methods are funtions that belong to a class and are used to perform actions related to the class.

def welcome(self):
    print("Welcome student")

s1 = Student("Prachi", 98)
s1.welcome = welcome  # Adding a method to the instance s1
s1.welcome(s1)  # Calling the method using the instance s1

#.................Static Methods in Python.................
# Static methods are methods that do not require an instance of the class to be called.
# methods that dont use the self parameter (work at class level)

class Student:
    @staticmethod
    def college():
        print("ABC University")
# Calling the static method without creating an instance of the class
Student.college()  # Output: ABC University
# Static methods can also be called using an instance of the class, but it is not recommended
s1 = Student()
s1.college()  # Output: ABC University (not recommended way)


#.....................IMPORTANT NOTE...................

# 1. ABSTRACTION: Hiding the complex implementation details and showing only the essential features of the object.

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    
    def start(self):
        self.clutch = True
        self.acc = True
        print("Car started")

car1 = Car()
car1.start()  # Output: Car started

# 2. ENCAPSULATION: Bundling the data (attributes) and methods (functions) that operate on the data into a single unit (class).

# 3. INHERITANCE: Mechanism to create a new class (child class) from an existing class (parent class) by inheriting its attributes and methods.

# 4. POLYMORPHISM: Ability to use a single interface to represent different data types or methods. 