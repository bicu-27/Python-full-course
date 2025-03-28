"""
Data types in python
Numeric 
Sequence type 
Boolean
Set
Dictionary


"""
# Numeric
# A data that has a numeric value.
#init 
#float 
# complex number
a = 5
print(type(a))
b = 3.4
print(type(b))
c = 3 + 5j
# Sequence type
# ordered collection of similar or different data types.
#string = represent unicode character.
string_one = "Welcome to my tutorial."
print(string_one)
# Accessing  elements of the string(We can make this using indexing.)
print(string_one[0])


#List = an ordered collection of data.
#List array of python.
fruit = ["apple","grape","lemon","orange"]
print(fruit[0])

# Tuple = they are the same with the list but we can't modified list.
# We can't change list after creating it.
tuple_one = ("freecodecamp","Geeks")
print(tuple(tuple_one))
# Boolean
# have two values either True or False
# Set 
# unordered collection of data.
# Set is mutable.
# Set is not indexed.
# Set is unchangeable(in structure).
# Set is iterable.\
# Set is not allow duplicate values.
# Set can be accessesd usnig for loop.
set1 = set("Geeks" "For ")
print(set1)
for i in set1:
    print(i)
# Dictionary
# Unordered collection of data.
# Used to store data value like map.
# Acollection of key value pair.
student = {
    "name" :"Lydia",
    "age " :21,
    "major" : "Software Engineer"
    
}

print(student["name"])





