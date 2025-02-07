#.............Range()..............

#-->Range function returns a numbers,starting from 0 by default and increments
#   by 1(by default),and stops before a specified number.
#range(start?,stop,step?)


for i in range(5): #range(stop)
    print(i)

# Output : 0,1,2,3,4

for i in range(2,10): #range(start,stop)
    print(i)

# Output : 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9

for i in range(2,10,2): #range(start,stop,step)
    print(i) 

# Output : 2 , 4 , 6 , 8
 
# Q. Print even numbers from 1 to 10.

for i in range(0,11,2): 
    print(i) 

# Output : 0, 2, 4, 6, 8, 10

#..........Lets Practice.............

#Q1. Print numbers from 1 to 100.

#ANSWER 

for i in range(0,101):
    print (i)

# Output : 0, 1, 2, 3, 4, 5,...100

# Q2. Print numbers from 100 to 1.

# Answer. 

for i in range(100,0,-1):
    print(i)

# Output : 100, 99, 98, 97, 96, 95,...1

# Q3. Print the multiplication table of a number n .

n = int(input("Enter the number : "))

for i in range(1,11):
    print(n*i)

# Output : Enter the number : 9 
#        9,18,27,36,45,54,63,72,81,90

#............Pass Statement .............

#--> Pass is a null statement that does nothing. It is used as placeholder for future code.

for i in range(4):
    pass # do nothing
print("Some useful work")

# Output : Some useful work

#..........Lets Practice .................

# Q1. WAP to find the sum of first n number .(using while)

# Using while loop.
n = 7
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1

    print("total sum = ",sum)

# Output : total sum = 28 

# Using for(): 

n = 10
sum = 0
for i in range (1,n+1):
    sum += i

print("total sum is ",sum) 

# Output : total sum is  55

# Q2. WAP to fing the factorial of first n  numbers. (using for)

n = 5
fact = 1
i = 1
while i<=n:
    fact *= i 
    i += 1
print ("Factorial",fact)

# Output : Factorial 120

n = 5
fact = 1 
for i in range(1,n+1):
    fact *= i
print("Factorial",fact)

# Output : Factorial 120