""" 
# Chapter 3
# positional argument

def user_info(name, age, city):

    '''This function prints name, age, and city from an argument provided to the function.'''

    print("{} is {} years old, from {}".format(name, age, city))

user_info("Phil", 21, "Miami")
user_info("DMX", 48)


# keyword arguments
# can define a default value for an argument in a function if a user does not provide a value for it
# position is not important when defining keyword arguments

def user_info(name, age=30, city="NYC"):

    '''This function prints name, age, and city from an argument provided to the function.'''

    print("{} is {} years old, from {}".format(name, age, city))

user_info("Phil", 21, "Miami")
user_info("DMX", 48)
user_info("Robin")
user_info(city="Dallas", name="John")


# *args and **kwargs
# *args = allows unlimited variables to be passed into a function without defining them
# **kwargs = allows unlimited keyword arguments to be passed into a function without defining them

def application(fname, lname, email, company, *args, **kwargs):
    print("{} {} works at {}. His email is {}.".format(fname, lname, company, email))

application("Michael", "Scott", "declareBankruptcy@work.com", "Dunder Mifflin", 75000, hire_date = "August 2003")



# Chapter 4
# conditionals / control structures - if/elif/else

name = input("What's your name? ")

if name == "Jessica":
    print("Hello, nice to see you {}".format(name))

elif name == "Danielle":
    print("Hello, you are a great person!")

elif name == "Kingston":
    print("Hi, {}, let's have lunch soon!".format(name))

else:
    print("Have a nice day!")


# Chapter 5
# loops and loop control

# for loop
# for {argument} in {list or range(a,b)}:

fruits = ["apple", "orange", "pears", "cherries", "grapes"]

for fruit in fruits:
    print("Would you like {} ?".format(fruit))
    
for number in range(1,9):
    print("Number {}".format(number))
    
# while loop
# while {argument}:

temp_f = 40
while temp_f > 32:
    print("The water is {} degrees.".format(temp_f))
    temp_f -= 1

# loop control
# break: end the loop; go to the next statement in the program (outside the loop)
# continue: skip current part of the loop; move to the next part of the loop
# pass: skip any part of the loop where "pass" appears; best used for testing code

for stat in range(1,11):
    if stat == 3:
        pass
    elif stat == 7:
        print("We're skipping stat 7.")
        continue
    elif stat == 9:
        break
    else:
        print("The stat is {}.".format(stat))
"""


# Chapter 6
# lists and list methods
# lists [{item1}, {item2}, etc.]- collection of items/data in brackets ; can contain all data types and other collections (lists, dict, tuples); mutable (items can be added/removed/changed); maintain order
# append method - add a single item to the list
# extend method - extend the list with another list
# remove method - remove item from the list
# pop method - remove item from the list based on their index number
# sort method - sort the list of like data types
# in method ({item} in list) - check membership in the list ; returns True or False
# count method - check membership in the list and count how many
# index method - check membership and index position in the list


# Chapter 7
# dictionaries and dictionaries methods
# dictionaries ({{key1:value1}, {key2:value2}, etc.}) - key/value pairings in brackets; keys have to be unique, immutable, and made of strings, integers, or typles; values can be any data type and mutable (items can be changed)
# get method - return the value of a key
# items method (dict.items()) - takes the name of the dictonary and outputs a view of the key/value pairs
# keys method (dict.keys()) - returns a view of all keys of the dict
# popitem method (dict.popitem()) - remove the last item in the dict
# setdefault method - see what the value is of a key and allow to set a default value when a key/value is not in a dict
# update method - update the dict; can also be used to add a secondary dict to the first dict


# Chapter 8
# Classes - group data and functions into a single unit; can also be shared with other classes; all classes are Objects; statements inside a class are usually functions, but can also contain class variables specific to the class and usable throughout
# instance variables - specific to any Objects that are created by the class
# inheritance - derived/child class can use attributes and methods of parent class; allows you to borrow from one class and use elements of that class to create another class
# multiple inheritance - derived/child class can inherit attributes and methods from more than one class; allows a class to inherit attributes from multiple classes
# polymorphism - derived/child classes can override class methods of parent class; allows inherited or derived classes to override the base or parent class
# __init__ method - a constructor and first method of a class; allows every instance of a class to be created/initialized with specific parameters; sets attributes for an object at object creation; generally used to set default state of object when it is created; must have two underscores on both sides of init;
# self variable - allows information to be shared; represents an instance of a class and references the instance of the class that has been created; used to make available all attributes to the methods throughout the class; if a method is running as part of the class rather than as an instance of the class, self is not needed
