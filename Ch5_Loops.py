#....................Loops in Python..............

count = 1
while count<=5 : 
    print("Hello") 
    count += 1 

print(count) # Output: 6

#print numbers from 1 to 5 

i = 1
while i<=5:
    print(i)
    i += 1 

print ("Loop completed") # Output: Loop completed


#....................Lets Practice ...............

#Q1. Print numbers from 1 to 100.

#ANSWER.

i = 1
while i<=100:
    print(i)
    i += 1
    
#Q2. Print numbers from 100 t0 1.

#ANSWER.

i=100
while i>=1: #Stopping condition.
    print(i)
    i -= 1

#Q3. Print the multiplication table of number n.

#ANSWER.

n=int(input("Enter the number of n : "))

i=1
while i<=10:
    print(n*i)
    i += 1

# Output : 
# Enter the number of n : 3
# 3
# 6
# 9
# 12
# 15
# 18
# 21
# 24
# 27
# 30

# Q4. Print the elements of the following list using a loop:
    #[ 1,4,9,16,25,36,49,64,81,100]

i = 1
while i<=10:
    print(i*i)
    i +=1   

# .............OR..............

nums = [ 1,4,9,16,25,36,49,64,81,100]

idx = 0
while idx<len(nums):
    print(nums[idx]) #Accessing elements using index.
    idx += 1

heroes = ["ironman","Thor","Loko","Harmin"]

i = 0 
while i<len(heroes):
    print(heroes[i])
    i += 1

#Q4. Search for a number x in this tuple using loop :

nums = (1,4,9,16,25,36,49,64,81,100)

x = 36

i = 0 
while i<len(nums):
    if nums[i] == x:
        print("Number found at idx",i)
    else:
        print("Finding...")
    i += 1


#.................Break & Continue............

# Break : used to terminate the loop when encountered.

i = 1
while i<=5:
    print(i)
    if(i==3):
        break # Terminating the loop when i is 3
    i += 1 
print("Loop terminated")


# Continue : Terminated execution in the current iteration & 
#           continues execution of the loop with the next iteration.

i = 0
while i<=5:
    
    if(i ==3):
        i += 1
        continue # skips the print statement
    print(i) # 
    i += 1

# Output :  0 1 2 4 5

i = 1
while i<=10:
    
    if(i%2 == 0 ):
        i += 1
        continue # skips the print statement
    print(i) #  
    i += 1

print("Loop terminated")  

# # Output :  1 3 5 7 9

i = 1
while i<=10:
    
    if(i%2 != 0 ):
        i += 1
        continue # skips the print statement
    print(i)
    i += 1

print("Loop terminated") 

# #Output : 2 4 6 8 10

#.......................FOR LOOPS...............

#--> Loops are used for Squential Traversal. For Traversing list,string,tuples.

nums = [1,2,3,4,5]

for val in nums:
    print(val)

tup = (12,33,11,33,26,11)

for val in tup:
    print(val)
else:
    print("Loop terminated")

#...............Let's Practice............(Using For Loop)

#Q1. Print the elements for the following list using a loop:

[1,4,9,16,25,36,49,64,81,100]

#Answer 

nums = [1,4,9,16,25,36,49,64,81,100]

for val in nums:
    print(val)

#Q2.Search for a number x in this tuple using a loop:

[1,4,9,16,25,36,49,64,81,100]

#Answer 

nums = [1,4,9,16,25,36,49,64,81,100,49]

x = 49
idx = 0
for el in nums:
    if(el == x):
        print("Number found at idx",idx)
        break
    idx += 1

