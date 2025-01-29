# ................Strings......................(Immutable)

str1 = "This is my string.\nthis is next line"
str2 = 'My name is Harmin\tGM'
str3 = """This is String 3"""

str4 = "Harmin"
str5 = "Patel"
final_str = str4 + " " + str5
print(final_str)
print(str1)
print(str2)
print(len(str4))

# ...................Indexing.................

str = "KPGU"
print(str[1])

# ...................Slicing..................

# => Acessing parts of a string.

str12="Code with me"
print(str12[:4]) #[0:5]
print(str12[5:]) #[5:len(str12)]

# Negative Index (Backward couting):

str11 = "apple"
print(str11[-4:-2])

#..................Some String Functions in Python...............:

str6="I am Studying in KPGU"
print(str6.endswith("GU")) #endswith Function

str7="i am Studying in KPGU"
str8=str7.capitalize() # capatilize Function
print(str8)

str9="I am studying Python in KPGU"
print(str9.replace("Python","Java")) #Replace Funtion

str10="I am studying Python in KPGU"
print(str10.find("KPGU")) #Find Function 

str13="I am studying Python in KPGU in Class 104"
print(str13.count("in")) #count Function(occurrence)


# ...........PRACTICE........

# Q1.WAP to input users first name and print its first name


a=input("Write your name:")
print("Length:",len(a))

#   WAP to find the occurence of '$' in a String.

str111="Hi, $ i am & symbol My cost is $100.99$"
print(str111.count("$"))

# ................Conditional Statements............

light="blue"

if(light=="red"):
    print("Stop")
elif(light=="green"):
    print("Go")
elif(light=="yellow"):
    print('Slow down')
else:
    print("Light is broken")

# Indetation : means using proper spacing while programming.


marks = float(input("Enter Your Marks:"))

if(marks>=95):
    grade="O"
elif(marks>=90):
    grade="A"
elif(marks>=80 and marks<90):
    grade="B"
elif(marks>=70 and marks<80):
    grade="C"
elif(marks>33 and marks<70):
    grade="D"
else:
    grade=("You are Failed")

print("Result of the student is :" ,grade )

# ............Nesting...........

age=int(input("Enter your age:"))

if(age>=18):
    if(age>=70):
        print("Cannot drive ")
    else:
        print("Can drive")
else:
    print("Cannot drive")
        
# .................... Lets Practice.............

# Q1.WAP to check if a number entered by the user is odd or even.

number=int(input("Enter random number:"))

if(number%2==0):
    print("Even")
else:
    print("Odd")

# Q2.WAP to find the Greatest of 3 numbers entered by the user.

a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c=int(input("Enter value of c:"))

if(a>=b and a>=c):
    print("A is greatest")
elif(b>=c):
    print("B is greatest")
else:
    print("C is greatest")

# Q3. WAP to check if a number is a multiple of 7 or not.

num=(int(input("Enter the number:")))

if(num%7==0):
    print("Multiple of 7")
else:
    print("Not a Multiple")