# .....................Dictionary in python.............
# ==> Dictionaries are used to store dta values in key:value pairs.
# ==> They are unordered , mutable & don't allow duplicate keys.

info={
    "name" : "KPGU",
    "Subjects":["python","C","Java"], #This is list in dictionary
    "Topics":("dict","Set"), #This is tuple in dictionary
    "learning" : "Coding",
    "age" : 21,
    "is_adult":True,
}

null_dict={}
# print(info)
print(info["name"])
info["name"]="Harmin"#overwrites the value.
info["surname"]="Patel"
print(info)

# ....................Nested dictionaries..............


student = { 
    "name" : "Harmin Patel",
    "subjects": {
        "phy": 95,
        "chem": 90,
        "math": 99,
    }
}
print (student)
print (student["subjects"]["chem"])

#...................Dictionary Methods...............

print(list(student.keys())) #returns all keys
# print(len(student))

print(list(student.values())) #returns all values

print(student.items()) #returns all key-value pairs
pairs = list (student.items())
print(pairs[0])

print(student["name"]) #returns value of key but gives ERROR
print(student.get("name")) #returns the value for the given key if it exists in the dictionary. If it does not,gives NONE

student.update({"city":"Vadodara","age":"21"}) #adds new key-value pair

print(student)

#.......................SET in PYTHON .........................

#--->Set is the collection of the unordered items.
#--->Each element in the set must be unique and immutable .
#--->Duplicate values are ignored in the set
#--->Set is mutable.

collection = {1,2,3,4,5,5,6,7,8,"hello","World"}


print(collection)
print(type(collection))
print(len(collection)) #returns the number of elements in the set

collection1 = set() #empty set

print(collection1)

#.................Set Methods.................

collection1.add(1) #adds an element to the set.
collection1.add(2)
collection1.add(2)
collection1.add(3)
collection1.add("HarminPatel")
collection1.add((1,2,3))

collection1.remove(2) #removes an element from the set.

collection1.clear() #clears all elements from the set.

# print(collection1)  

collection2 = {"Python","Anaconda","hello","World"}
collection2.pop() #removes and returns an arbitrary element from the set.

print(collection2) 

print(collection.union(collection2)) #returns a new set with elements from both sets.

print(collection.intersection(collection2)) #returns a new set with elements common to both sets.


# ..................Lets Practice...................

# Q1. Store following word meanings in Python dictionary . 

# table : "a piece of furniture","list of facts & figures"
# cat : "a small animal"

# Answer:

my_dict={
    "table":["a piece of furniture","list of facts & figures"],
    "cat":"a small animal"
}
print(my_dict)

#Q2. You are given a list of subjects for students.Assume one classroom is
#   required for 1 subject . How many classrooms are needed by all students. 

#"python","java","C++","javascript",
# "java",python","java","C++","C"    

#ANSWER

subjects={
    "python","java","C++","javascript","java","python","java","C++","C"
}
print(subjects)
print(len(subjects))

#Q3.WAP to enter marks of 3 subjects from the user and store them in a dictionary.
#  Start with an empty dictionary & add one by one . use subject name as key and 
# marks as a value.

#ANSWER

marks={}

x= int(input("enter phy :"))
marks.update({"phy":x})

x= int(input("enter math:"))
marks.update({"math":x})

x= int(input("enter chem:"))
marks.update({"chem":x})

print(marks)


#Q4. Figure out a way to store 9 and 9.0 as a separate values in the set .
#   (you can take help of built-in data types)

#ANSWER

values = {9,"9.0"}
print(values)

# ........OR.........

values1 = {
    ("float",9.0),
    ("int",9)
}
print(values1)  