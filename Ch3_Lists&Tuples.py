# ..............Lists in Python:................
 
# ==> A built in data type that stores set of values.
# ==> It can store elemets of different types
#     (int,float,string,etc.)
# ==>Lists are MUTABLE.

marks=[89.3,34.4,87.5,90.3,43.4]
print(marks)
print(type(marks))
print(marks[1])
print(marks[0])

student=["Harmin",99.32,21,"Vadodafra"]
print(student)
student[0]="Arjun"
print(student)
print[student[5]]

# ..................List slicing..............
# ==>Ending index in not included.

marks=[87,34,55,32,12,43]
print(marks[3:5])

# ...............List Methods:..............

list = [2,4,6]
list.append(3)  #Append Method : To Add a object in a string.
print(list)

list = [9,2,93,55]
list.sort() #Sorting Method (Ascending Order)
print(list)

list = [2,6,4,8,5,9]
list.sort(reverse=True)  # Sort - Reverse Method (Descending Order)
print(list)

list = [ 3,2,4,1,5]
list.reverse() # Reverse Method(Exactly reverses the list)
print(list)

list = [2,1,3]
list.insert(1,5) # Insert method ( Insert the element before 1 & and print
                    #prints the you want to insert)
print(list)

list= [ 2,3,1,4,2]
list.remove(2) #Removes first occurence of element : (3,1,4,2)
print(list)

list = [ 3,2,1,5,4]
list.pop(2) # deletes the element at index
print(list)

# ................TUPLES in Python:............

# ===> A built in data type that lets us create immutable 
# sequences of values.
# ==> Tuples are Immutable.

tup = ( 2,3,1,5)
print(tup[0])
print(tup[1])

tup = (1,)
tup1 = (2,1,3)
print(tup)
print(type(tup))
print(type(tup1))

#.............Tuple Methods..........

tup = (2,1,4,5)
print(tup.index(4)) #Returns index of first occurence 

tup = ( 3,4,2,3,11,3)
print(tup.count(3)) # Counts totsl occurences

# ...........Lets Practice..............
# Q1.WAP to ask the user enter names of their 3 fav movies & 
#   store them in a list.

movies = [] 
list1 = (str(input("Enter the name of your first fav movie:")))
list2 = (str(input("Enter the name of your second fav movie:")))
list3 = (str(input("Enter the name of your third fav movie:")))

movies.append(list1)
movies.append(list2)
movies.append(list3)

print(movies)

# Q2. WAP to check if a list contains a palindrome of elements.
#     (hints: use copy()method )

# Example 1:
list1 = [1,2,1]
list2 = [1,2,3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1==list1):
    print("Its Palindrome")
else:
    print("Not Palindrome")

# Example 2 :
list1 = [1,2,3]


copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1==list1):
    print("Its Palindrome")
else:
    print("Not Palindrome")

# Q3.WAP to count the number of students with the "A" grade in the 
#   following tuple.
#   ["c","d","a","b","b","a"]

tup = ["c","d","a","b","b","a"]
print(tup.count("b"))

# Q4.Store the above Values in list & sort them from "a" to "d".

list = ["c","d","a","b","b","a"]
print(list.sort())
print(list)