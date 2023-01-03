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
# __init__ method (def __init__(self, {positional arguments}, etc.)- a constructor and first method of a class; allows every instance of a class to be created/initialized with specific parameters; sets attributes for an object at object creation; generally used to set default state of object when it is created; must have two underscores on both sides of init;
# self variable - allows information to be shared; represents an instance of a class and references the instance of the class that has been created; used to make available all attributes to the methods throughout the class; if a method is running as part of the class rather than as an instance of the class, self is not needed

import random


class Person:
    def __init__(self, firstname, lastname, health, status):
        "Initializes attributes to be used in for all class methods in this class and for class Objects created by this class. self will make those attributes available in the __init__ method and other methods."
    
        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status
    
    
    def introduce(self):
        "All people introduce themselves."
        
        print("Hi, I'm {} {}.".format(self.firstname, self.lastname))
        
        
    def emote(self):
        "Giving each person the ability to have an emotion."
        
        emotion = random.randrange(1, 3)
        
        if emotion == 1:
            print("{} is happy today.".format(self.firstname))
        
        elif emotion == 2:
            print("{} is sad right now.".format(self.firstname))
            

    def status_change(self):
        "Prints a message based on health score for the person."
        
        if self.health == 100:
            print("{} is totally healthy!".format(self.firstname))

        elif self.health >=76:
            print("{} is a little tired today.".format(self.firstname))

        elif self.health >= 51:
            print("{} feels unwell.".format(self.firstname))

        elif self.health >= 40:
            print("{} goes to the doctor".format(self.firstname))

        else:
            print("{} is unconscious.".format(self.firstname))
        
        
# creating a person by using the Person class
Maria = Person("Maria", "Rodriguez", 65, status=True)
Pierre = Person("Pierre", "Rodriguez", 88, status=True)
Junior = Person("Junior", "Rodriguez", 100, status=True)

print("{} is my relative? {}".format(Maria.firstname, Maria.status))
print("{} is my relative? {}".format(Pierre.firstname, Pierre.status))
print("{} is my relative? {}".format(Junior.firstname, Junior.status))

# after creating each person, you can access other methods by using Person.method and replace Person with a person
Maria.introduce()
Pierre.introduce()
Junior.introduce()

Maria.status_change()
Pierre.status_change()
Junior.status_change()



# Chapter 9
# Inheritance / Multiple Inheritances / Polymorphism
# inheritance - use attributes and methods from parent class and make them available to the child's class
# super method - access all attributes from the parent class

import random

# parent class
class Person:
    def __init__(self, firstname, lastname, health, status):
        'Initializes attributes to create a new person.'
        
        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status
        
    
    def introduce(self):
        'Introduction for said person.'
        
        print("Hi, I'm {} {}.".format(self.firstname, self.lastname))
        
        
    def emote(self):
        'Expressing two kinds of emotions.'
        
        emotion = random.randrange(1, 3)
        
        if emotion == 1:
            print('{} is happy today.'.format(self.firstname))
        
        elif emotion == 2:
            print('{} is sad right now.'.format(self.firstname))
        
            
    def status_change(self):
        'Prints a message based on health score for the person.'
        
        if self.health == 100:
            print('{} is totally healthy!'.format(self.firstname))

        elif self.health >=76:
            print('{} is a little tired today.'.format(self.firstname))

        elif self.health >= 51:
            print('{} feels unwell.'.format(self.firstname))

        elif self.health >= 40:
            print('{} goes to the doctor'.format(self.firstname))

        else:
            print('{} is unconscious.'.format(self.firstname))
        


# child class
class Enemy(Person):
    def __init__(self, weapon, firstname, lastname, health, status):
        super().__init__(firstname, lastname, health, status)
        'A child class inheriting from Person class to create an enemy.'
        
        self.weapon = weapon
        
    
    def hurt(self, other):
        'Attacks and reduces said person"s health.'
        
        if self.weapon == 'rock':
            other.health -= 10
        
        elif self.weapon == 'stick':
            other.health -= 5
            
        print('{} attacked {} and reduced their health to {}.'.format(self.firstname, other.firstname, other.health))
        
        
    def insult(self, other):
        'Insulting said person.'
        
        if other.health <= 80:
            print('{} insulted {} and said they are tired and weak.'.format(self.firstname, other.firstname))
            
        else:
            print('{} told {} that they should be happy that they are stronger than him.'.format(self.firstname, other.firstname))
            
            
    def steal(self, other):
        'Stealing from said person.'
        
        print('{} laughed at {} as they proclaimed that they stole their stuff.'.format(self.firstname, other.firstname))
        
        if other.status == True:
            other.status == False
            

Maria = Person("Maria", "Rodriguez", 65, status=True)
Pierre = Person("Pierre", "Rodriguez", 88, status=True)
Junior = Person("Junior", "Rodriguez", 100, status=True)            
Alex = Enemy('rock', 'Alex', 'Smith', 75, status=False)
Alex.hurt(Maria)
Alex.insult(Pierre)
Alex.insult(Maria)
Alex.steal(Junior)


# Multiple Inheritance
# inherit from multiple classes and able to use attributes and methods from multiple classes
# the order of inheritance matters

# Parent class 1
class Item():

    def __init__(self, sku):
        self.sku = sku

    def print_sku(self):
        print("The sku is {}.".format(self.sku))
        

# Parent class 2
class Garment():

    def __init__(self, section, type):
        self.section = section
        self.type = type

    def print_garment(self):
        print("The garment is in section {}, {}.".format(self.section, self.type))
        

# Child Class
class Shirts(Item, Garment):

    def __init__(self, name, color, sku, section, type):
        self.name = name
        self.color = color

        Item.__init__(self, sku)
        Garment.__init__(self, section, type)

    def print_shirt(self):
        print("{} {} on sale!".format(self.color, self.name))
        
        
Blouse = Shirts('Formal Blouse', 'White', '00001', 43, 'Tops')
Blouse.print_sku()
Blouse.print_garment()
Blouse.print_shirt()
"""


# Polymorphism
# method overriding; occurs when a child class has a method with the same name and implementation as the parent class and you want override the parent class method

import random

# parent class
class Person:
    def __init__(self, firstname, lastname, health, status):
        'Initializes attributes to create a new person.'
        
        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status
        
    
    def introduce(self):
        'Introduction for said person.'
        
        print("Hi, I'm {} {}.".format(self.firstname, self.lastname))
        
        
    def emote(self):
        'Expressing two kinds of emotions.'
        
        emotion = random.randrange(1, 3)
        
        if emotion == 1:
            print('{} is happy today.'.format(self.firstname))
        
        elif emotion == 2:
            print('{} is sad right now.'.format(self.firstname))
        
            
    def status_change(self):
        'Prints a message based on health score for the person.'
        
        if self.health == 100:
            print('{} is totally healthy!'.format(self.firstname))

        elif self.health >=76:
            print('{} is a little tired today.'.format(self.firstname))

        elif self.health >= 51:
            print('{} feels unwell.'.format(self.firstname))

        elif self.health >= 40:
            print('{} goes to the doctor'.format(self.firstname))

        else:
            print('{} is unconscious.'.format(self.firstname))
        


# child class
class Enemy(Person):
    def __init__(self, weapon, firstname, lastname, health, status):
        super().__init__(firstname, lastname, health, status)
        'A child class inheriting from Person class to create an enemy.'
        
        self.weapon = weapon
        
    
    def introduce(self):
        'Intro method will override the parent class method.'
        
        print('My name is {} {}. You killed my father. Prepare to die.'.format(self.firstname, self.lastname))
    
    
    def hurt(self, other):
        'Attacks and reduces said person"s health.'
        
        if self.weapon == 'rock':
            other.health -= 10
        
        elif self.weapon == 'stick':
            other.health -= 5
            
        print('{} attacked {} and reduced their health to {}.'.format(self.firstname, other.firstname, other.health))
        
        
    def insult(self, other):
        'Insulting said person.'
        
        if other.health <= 80:
            print('{} insulted {} and said they are tired and weak.'.format(self.firstname, other.firstname))
            
        else:
            print('{} told {} that they should be happy that they are stronger than him.'.format(self.firstname, other.firstname))
            
            
    def steal(self, other):
        'Stealing from said person.'
        
        print('{} laughed at {} as they proclaimed that they stole their stuff.'.format(self.firstname, other.firstname))
        
        if other.status == True:
            other.status == False
            

Maria = Person("Maria", "Rodriguez", 65, status=True)
Pierre = Person("Pierre", "Rodriguez", 88, status=True)
Junior = Person("Junior", "Rodriguez", 100, status=True)            
Alex = Enemy('rock', 'Alex', 'Smith', 75, status=False)

Maria.introduce()
Pierre.introduce()
Alex.introduce()
