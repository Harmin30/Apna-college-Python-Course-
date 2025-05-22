#...........Functions in Python...........
#--> Block of statements that perform a specific task.
#--> Functions are reusable blocks of code.
#--> Functions can take arguments and return values.
#--> Functions can be defined inside other functions.
#--> Functions can be defined inside classes.
#--> Parameters are optional in function.
#--> Return statments can be optional in function.

def calc_sum(a,b):
    sum = a + b
    print(sum)
    return sum 

calc_sum(2 , 10)

#--> Output: 12

#more lines of code 

calc_sum(123 , 932)

#--> Output: 1055

#more lines of code

calc_sum(87,13)

#--> Output: 100

#Function definition:

def calc_sum(a,b): #parameters
    return a + b

sum = calc_sum(1,4) #function call; arguments
print(sum)

def print_hello():
    print("hello")

output = print_hello()
print(output) #None

# Q. Average of 3 numbers :

def calc_avg(a,b,c):
    sum = a+b+c
    avg = sum/3
    print(avg)
    return avg

calc_avg(4,5,1)

# Output : 3.3333333333333335

#...................Types of functions..........

#--->1. Built-in functions : These are functions that are already defined in python.
#--->2. User-defined functions : These are functions that are defined by the user.

#..............Default Parameters.............
#---> Assigning a default value to parameters , which is used when no arguement is passed.

def cal_prod(a=1,b=1): #default parameters
    print(a*b)
    return a*b 

cal_prod(2,4)

# Output : 8

# ...................Let's Practice................

# Q1. WAF to print the length of a list. ( list is the parameter)

cities = ["baroda","anand","mumbai","delhi","Pune"]
planets = ["earth","mars","jupiter"]

def print_len(list):
    print(len(list))

print_len(cities) #6
print_len(planets) #3 

# Output : 6
# Output : 3

# Q2. WAF to print the elements of a list in a single line. ( list is the parameter)

planets = ["earth","mars","jupiter"]
cities = ["baroda","anand","mumbai","delhi","Pune"]
heros = ["thor","ironman","shaktiman"]

def print_len(list): 
    print(len(list))

def print_list(list):
    for item in list : 
        print(item,end=" ") #end=" " is used to print elements in a single line

print_list(cities)
print_list(planets)
print_list(heros) 

# Output : baroda anand mumbai delhi Pune earth mars jupiter thor ironman shaktiman

# Q3.WAF to find the factorial of n. (n is the parameter)

def cal_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(" ")
    print(fact) 
    return fact

cal_fact(5) 

# Output : 120

# Q4.WAF to convert USD to INR.

# exchange rate is 1 USD = 86 INR

def converter(usd_val):
    inr_val = usd_val * 86
    print(usd_val ,"USD = ", inr_val," INR" )

converter(100) 

# Output : 100 USD =  8600.0 INR
 
# ........................Recursion.................................

#---> A function that calls itself is called a recursive function.

def show(n):
    if (n == 0): #base case 
        return
    print(n)
    show(n-1) #recursive call

show(5)
#--> Output : 5 4 3 2 1
    #--> The function will keep calling itself until the base case is reached.

# Factorial using recursion
def fact(n):
    if (n == 0 or n == 1): #base case
        return 1
    else:
        return n * fact(n-1) #recursive call
print(fact(5)) #120
#--> Output : 120

# ............let's Practice Recursion.................

# Q1. WAF to find the sum of first n natural numbers using recursion.

def calc_sum(n):
    if(n== 0):
        return 0
    else:
        return n + calc_sum(n-1)
    
print(calc_sum(5)) 
#--> Output : 15

# Q2. Write a recursive function to print all elements in a list .
# Hint : use list and index as parameters.

def print_list(list,index):
    if (index == len(list)):
        return
    print(list[index])
    print_list(list,index+1)
cities = ["baroda","anand","mumbai","delhi","Pune"]
print_list(cities,0)

#--> Output : baroda anand mumbai delhi Pune