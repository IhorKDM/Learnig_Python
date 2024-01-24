######################################################################################################
# import time
#TUTORIAL
######################################################################################################
#print('I love pizza')
#print('It is very delicious')
######################################################################################################

    #VARIABLES N.1
######################################################################################################
# name = 'Bro'
# print(type(name))
# print('Hello ' + name)
#
# age = 21
# age += 1
# print('Your age is: ' +str(age))
# print(type(age))
#
# height = 173.4
# print('Your height is: '+ str(height)+ "cm")
# print(type(height))
#
# human = True
# print('Are you a human: ' + str(human))
# print(type(human))
######################################################################################################

    #VARIABLES N.2
######################################################################################################
# name = "Bro"
# age = 21
# attractive = True
# print(name)
# print(age)
# print(attractive)
#
# name, age, attractive = "Bro", 21, True
# print(name)
# print(age)
# print(attractive)
#
# Spongebob = 30
# Patrick = 30
# Sandy = 30
# Squidward = 30
# print(Spongebob)
# print(Patrick)
# print(Sandy)
# print(Squidward)
#
# Spongebob = Patrick = Sandy = Squidward =30
# print(Spongebob)
# print(Patrick)
# print(Sandy)
# print(Squidward)
######################################################################################################

    #STRING METHODS
######################################################################################################
# name = "Bro Code"
#
# print(len(name))
# print(name.find('o'))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count('o'))
# print(name.replace("o",'a'))
# print(name*3)
######################################################################################################

    #TYPE CASTING
######################################################################################################
# x =1 #int
# y =2.0 #float
# z = "3" #str
#
# print("X is " + str(x))
# print("Y is "+ str(y))
# print(z*3)
######################################################################################################

# name = str(input("What is your name ")).capitalize()
# age = int(input("How old are you"))
# height = float(input("How tall are you"))
#
# print('Hello '+ name)
# print("You are "+ str(age) + ' years old' )
# print("You are " + str(height) + "cm tall")
######################################################################################################

    #MATH FUNCTION
######################################################################################################
# import math
#
# pi = 3.14
# x =1
# y = 2
# z = 3
#
# print(round(pi))
# print(math.ceil(pi))
# print(math.floor((pi)))
# print(abs(pi))
# print(pow(pi,2))
# print(math.sqrt(420))
# print(max(x,y,z))
# print(min(x,y,z))
######################################################################################################

    #STRING SLICING
######################################################################################################
# name = 'Bro Code'
#
# first_name = name[:3]
# last_name = name[4:]
# fanName = name[::2]
# reversedName = name[::-1]
#
# print(first_name)
# print(last_name)
# print(fanName)
# print(reversedName)
#
#
# website = "http://google.com"
#
# slice = slice(7, 13)
# print(website[slice])
######################################################################################################

    #IF STATEMENTS
######################################################################################################
# age = int(input('How old are you'))
#
# if age == 100:
#     print('You are century old man')
# elif age >= 18:
#     print('You are adult')
# elif age < 0:
#     print("You are not born yet")
# else:
#     print('You are a child')
######################################################################################################

    #LOGICAL OPERATORS
######################################################################################################
# temp = int(input("What is temp outside"))
#
# if temp >= 0 and temp <= 30:
#     print('The weather is good togay!')
#     print('Go outside')
# elif temp < 0 or temp > 30:
#     print("The temp is bad today!")
#     print("Stay home")
######################################################################################################

    #WHILE LOOP
######################################################################################################
# name = None
#
# while not name:
#     name = input('Enter your name')
#
# print('Hello '+ name)
######################################################################################################

    #FOR LOOP
######################################################################################################
# import time
#
# for i in range(10+1):
#     print(i)
#
# for i in range(50, 100+1,2):
#     print(i)
#
# for i in 'Bro Code':
#     print(i)
#
# for i in range(10,-1,-1):
#     print(i)
#     time.sleep(1)
# print('Happy NEW YEAR')
######################################################################################################

    #NESTED LOOP
######################################################################################################
# rows = int(input('`how many rows'))
# colums = int(input('`how many columns'))
# symbol = input("Symbol")
#
# for i in range(rows):
#     for j in range(colums):
#         print(symbol, end='')
#     print()
######################################################################################################

    #LOOP CONTROL STATEMENTS
######################################################################################################
# while True:
#     name = input('Enter name')
#     if name != "":
#         break
#
# phone_number = '123-456-789-000'
#
# for i in phone_number:
#     if i == '-':
#         continue
#     print(i,end='')
#
# for i in range(1,21):
#     if i == 13:
#         pass
#     else:
#         print(i)
######################################################################################################

    #LIST
######################################################################################################
# food = ['pizza','spaghetti', 'hotdog' ,'hamburger', 'pudding']
# food[0] = 'sushi'
#
# print(food[0])
# food.append('ice-cream')
# food.remove('hotdog')
# food.pop()
# food.insert(0,'cake')
# food.sort()
# food.clear()
#
# for x in food:
#     print(x)
######################################################################################################

    #2D-LIST
######################################################################################################
# drinks = ['coffee', 'soda', 'tea']
# dinner = ['pizza', 'hamburger', 'hotdog']
# dessert = ['cake', 'ice-cream']
#
# food = [drinks,dinner,dessert]
#
# print(food[2][1])
######################################################################################################

    #TUPLE
######################################################################################################
# student = ("Bro",21,"male")
#
# print(student.count('Bro'))
# print(student.index('male'))
#
# for x in student:
#     print(x)
#
# if "Bro" in student:
#     print("Bro is here")
######################################################################################################

    #SET
######################################################################################################
# utensils = {"fork", 'spoon', 'knife'}
# dishes = {'bowl', 'plate', 'cup', 'knife'}
#
# utensils.add('napkin')
# utensils.remove('fork')
# utensils.clear()
# utensils.update(dishes)
# dinner_table = utensils.union(dishes)
# print(utensils.difference(dishes))
# print(dishes.difference(utensils))
# print(utensils.intersection(dishes))
#
# for x in dinner_table:
#     print(x)
######################################################################################################

    #DICTIONARY
######################################################################################################
# capitals = {'USA' : 'Washington DC',
#             'India' : 'New Dehli',
#             'China' : 'Beijing',
#             'Ukraine' : 'Kyiv'}
#
# print(capitals['Germany'])
# print(capitals.get('Germany'))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())
#
# capitals.update({'Germany' : 'Berlin'})
# capitals.update({'USA':'Las Vegas'})
# capitals.pop('China')
# capitals.clear()
#
# for key, value in capitals.items():
#     print(key, value)
######################################################################################################

    #INDEX OPERATOR
######################################################################################################
# name = 'bro Code!'
#
# if (name[0].islower()):
#     name = name.capitalize()
# first_name = name[:3].upper()
# last_name = name[4:].upper()
# lastChar = name[-1]
#
# print(lastChar)
# print(name)
# print(first_name)
# print(last_name)
######################################################################################################

    #FUNCTIONS
######################################################################################################
# def hello(First_name, Last_name, age):
#     print('Hello! ' + First_name + " " + Last_name)
#     print('You are ' + str(age) + ' years old')
#     print('Have a nice day')
#
# my_name = 'Bro'
# hello('Bro', 'Code', 21)
######################################################################################################

    #RETURN STATEMENTS
######################################################################################################
# def multiply(num1, num2):
#     return num1 * num2
#
# x = multiply(6,8)
#
# print(x)
######################################################################################################

    #KEYWORD ARGUMENTS
######################################################################################################
# def hello(first, middle, last):
#     print('Hello ' + first + ' ' + middle + " " + last)
#
# hello(first='Bro', last='Dude', middle='Code')
######################################################################################################

    #NESTED FUNCTIONS CALLS
######################################################################################################
# num = input('Enter a whole positive number: ')
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)
#
# print(round(abs(float(input('Enter a whole positive number: ')))))
######################################################################################################

    #SCOPE
######################################################################################################
# name = "Bro"
# def display_name():
#     name = 'Code'
#     print(name)
#
# display_name()
# print(name)
######################################################################################################

    #*ARGS - for function
######################################################################################################
# def add(*stuff):
#     sum = 0
#     stuff = list(stuff)
#     stuff[0] = 0
#     for i in stuff:
#         sum += i
#     return sum
#
# print(add(1,2,3,6,7,9,123))
######################################################################################################

    #**kwargs - for dictionary
######################################################################################################
# def hello(**kwargs):
#     print('Hello ' + kwargs['first'] + ' ' + kwargs['last'])
#     print('Hello', end=' ')
#     for key,value in kwargs.items():
#         print(value, end=' ')
#
# hello(title='Mr.', first="Bro", middle='Dude' ,last='Code')
######################################################################################################

    #STR.FORMAT
######################################################################################################
# animal = 'cow'
# item = 'moon'
#
# print('The '+animal+" jumped over the "+item)
# print('The {} jumped over the {}'.format(animal,item))
# print('The {1} jumped over the {1}'.format(animal,item)) #positional arguments
# print('The {animal} jumped over the {item}'.format(animal='cow',item='moon')) #keyword arguments
#
# text = 'The {} jumped over the {}'
# print(text.format(animal,item))
#
# name = "Bro"
#
# print('Hello, my name is {}'.format(name))
# print('Hello, my name is {:10}. Nice to meet you'.format(name))
# print('Hello, my name is {:<10}. Nice to meet you'.format(name))
# print('Hello, my name is {:>10}. Nice to meet you'.format(name))
# print('Hello, my name is {:^10}. Nice to meet you'.format(name))
#
# numb = -117
#
# print('The number pi is {:.3f}'.format(numb))
# print('The number is {:,}'.format(numb))
# print('The number is {:b}'.format(numb))
# print('The number is {:o}'.format(numb))
# print('The number is {:X}'.format(numb))
# print('The number is {:E}'.format(numb))
######################################################################################################

    #RANDOM NUMBERS
######################################################################################################
# import random
#
# x = random.randint(1,6)
# y = random.random()
#
# myList = ['rock', 'paper', 'scissors']
# z = random.choice(myList)
#
# cards = [1,2,3,4,5,6,7,8,9,'J','Q','K','A']
#
# random.shuffle(cards)
#
# print(cards)
# print(z)
# print(y)
# print(x)
######################################################################################################

    #EXCEPTIONS
######################################################################################################
# try:
#     numerator = int(input('Enter a number to divide: '))
#     denominator = int(input('Enter a number to divide by: '))
#     result = numerator / denominator
# except ZeroDivisionError as e:
#     print(e)
#     print('You cannot divide by zero! idiot!')
# except ValueError as e:
#     print(e)
#     print("Enter only number please")
# except Exception as e:
#     print(e)
#     print('Somethin went wrong :(')
# else:
#     print(result)
# finally:
#     print('That is good')
######################################################################################################

    #FILE DETECTIONS
# ######################################################################################################
# import os
#
# path = "/Users/ihorkdm/Desktop/file.txt"
#
# if os.path.exists(path):
#     print('That location exist!')
#     if os.path.isfile(path) :
#         print('That is a file!')
#     elif os.path.isdir(path):
#         print('That is a directory!')
# else:
#     print('That location does not exist!')
######################################################################################################

    #READ A FILE
######################################################################################################
# try:
#     with open('test.txt') as file:
#         print(file.read())
# except FileNotFoundError:
#     print('File is not detected')
######################################################################################################

    #WRITE A FILE
######################################################################################################
# text = 'Have a nice day'
# with open('test.txt','a') as file:
#     file.write(text)
######################################################################################################

    #COPY A FILE
######################################################################################################
# import shutil
#
# shutil.copy('test.txt','copy.txt')
######################################################################################################

    #MOVE A FILE
######################################################################################################
# import os
#
# source = 'folder'
# destination = '/Users/ihorkdm/Desktop/folder'
#
# try:
#     if os.path.exists(destination):
#         print('There is already a file there')
#     else:
#         os.replace(source,destination)
#         print(source+ ' was moved')
# except FileNotFoundError:
#     print(source+ 'Was not found')
######################################################################################################

    #DELETE FILE
######################################################################################################
#import os
# import shutil
#
#path = 'copy.txt'
#
# try:
#     os.remove(path)
#     os.rmdir(path)
#     shutil.rmtree(path)
# except FileNotFoundError:
#     print('That file was not found')
# except PermissionError:
#     print('You do not have permision to delete it')
# except OSError:
#     print('You cannot delete that using thatvfunction')
# else:
#     print(path+" was deleted")
######################################################################################################

    #MODULES
######################################################################################################
# from messages import *
#
# hello()
# bye()
#
# help('modules')
######################################################################################################

    #ROCK, PAPER, SCISSORS GAME
######################################################################################################
# import random
#
# while True:
#
#     choices = ['rock', 'paper', 'scissors']
#
#     computer = random.choice(choices)
#     player = None
#
#     while player not in choices:
#         player = input('rock, paper, scissors?: ').lower()
#
#     if player == computer:
#         print('computer:',computer)
#         print('player:',player)
#         print('Tie!')
#     elif player == 'rock':
#         if computer == 'paper':
#             print('computer:', computer)
#             print('player:', player)
#             print('you lose!')
#         if computer == 'scissors':
#             print('computer:', computer)
#             print('player:', player)
#             print('you win!')
#     elif player == 'scissors':
#         if computer == 'rock':
#             print('computer:', computer)
#             print('player:', player)
#             print('you lose!')
#         if computer == 'paper':
#             print('computer:', computer)
#             print('player:', player)
#             print('you win!')
#     elif player == 'paper':
#         if computer == 'scissors':
#             print('computer:', computer)
#             print('player:', player)
#             print('you lose!')
#         if computer == 'rock':
#             print('computer:', computer)
#             print('player:', player)
#             print('you win!')
#
#     play_again = input('Play again? (yes/no): ').lower()
#
#     if play_again != 'yes':
#         break
# print('Bye')
######################################################################################################

    #QUIZ GAME
######################################################################################################
# def new_game():
#
#     guesses = []
#     correct_guesses = 0
#     question_num = 1
#
#     for key in questions:
#         print('--------------------------------------------------')
#         print(key)
#         for i in options[question_num-1]:
#             print(i)
#
#         guess = input("Enter (A, B, C, D")
#         guess = guess.upper()
#         guesses.append(guess)
#
#         correct_guesses += check_answer(questions.get(key),guess)
#         question_num += 1
#
#     display_score(correct_guesses, guesses)
# #--------------------------------------------------
# def check_answer(answer, guess):
#
#     if answer == guess:
#         print('Correct')
#         return 1
#     else:
#         print('Wrong')
#         return 0
# #--------------------------------------------------
# def display_score(correct_guesses, guesses):
#     print('--------------------------------------------------')
#     print('Resulsts')
#     print('--------------------------------------------------')
#
#     print('Answers: ', end='')
#     for i in questions:
#         print(questions.get(i), end=' ')
#     print()
#
#     print('Guesses: ', end='')
#     for i in guesses:
#         print(i, end=' ')
#     print()
#
#     score = int((correct_guesses/len(questions))*100)
#     print('Your score is: ', score)
# #--------------------------------------------------
# def play_again():
#
#     response = input('Do you want to play again? (Yes/No): ')
#     response = response.upper()
#
#     if response == 'YES':
#         return True
#     else:
#         return False
# #--------------------------------------------------
#
# questions = {
#     'Who created Python?: ': 'A',
#     'What year was Python created?: ': 'B',
#     'Python is tributed to which comedy group?: ': 'C',
#     'Is the Earth round?: ': 'A'
# }
#
# options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
#            ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
#            ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
#            ["A. True", "B. False", "C. sometimes", "D. What is Earth?"]]
#
# new_game()
# while play_again():
#     new_game()
#
# print('Bye')
######################################################################################################

    #OBJECT ORIENTED PROGRAMMING(OOP)
######################################################################################################
# from messages import Car
#
# car_1 = Car('Chevy', 'Corvette', 2021, 'blue')
# car_2 = Car("Ford", 'Mustang', 2022, 'red')
#
#
#
# car_1.drive()
# car_2.stop()
######################################################################################################

    #CLASS VARIABLES
######################################################################################################
# from messages import Car
#
# car_1 = Car('Chevy', 'Corvette', 2021, 'blue')
# car_2 = Car("Ford", 'Mustang', 2022, 'red')
#
# #car_1.wheels = 2
# #print(car_1.wheels)
# #print(car_2.wheels)
# Car.wheels = 2
#
# print(car_1.wheels)
# print(car_2.wheels)
######################################################################################################

    #INHERITANCE
######################################################################################################
# class Animal:
#     alive = True
#
#     def eat(self):
#         print('This animal is eating')
#
#     def sleep(self):
#         print('This animal is a sleeping')
#
# class Rabbit(Animal):
#     def run(self):
#         print('This rabbit is running')
# class Fish(Animal):
#     def swim(self):
#         print('This fish is swimming')
# class Hawk(Animal):
#     def fly(self):
#         print('This hawk is fling')
#
# rabbit = Rabbit()
# fish = Fish()
# hawk = Hawk()
#
# print(rabbit.alive)
# fish.eat()
# hawk.sleep()
#
# rabbit.run()
# fish.swim()
# hawk.fly()
######################################################################################################

    #MULTILEVEL INHERITANCE
######################################################################################################

# class Organism:
#     alive = True
#
# class Animal(Organism):
#     def eat(self):
#         print('This animal is eating')
#
# class Dog(Animal):
#     def bark(self):
#         print('This dog is barking')
#
# dog = Dog()
# print(dog.alive)
# dog.eat()
# dog.bark()
######################################################################################################

    #MULTIPLE INHERITANCE
######################################################################################################
# class Prey:
#     def flee(self):
#         print('This animal flees')
#
# class Predator:
#     def hunt(self):
#         print("This animal is hunting")
#
# class Rabbit(Prey):
#     pass
#
# class Hawk(Predator):
#     pass
#
# class Fish(Prey, Predator):
#     pass
#
# rabbit = Rabbit()
# hawk = Hawk()
# fish = Fish()
#
# rabbit.flee()
# hawk.hunt()
# fish.flee()
# fish.hunt()
######################################################################################################

    #METHOD OVERRIDING
######################################################################################################
# class Animal:
#     def eat(self):
#         print('This animal is eating')
#
# class Rabbit(Animal):
#     def eat(self):
#         print('This rabbit is eating a carrot')
#
# rabbit = Rabbit()
# rabbit.eat()
######################################################################################################

    #METHOD CHAINING
######################################################################################################
# class Car:
#     def turn_on(self):
#         print("You start the engine")
#         return self
#
#     def drive(self):
#         print('You drive the car')
#         return self
#
#     def brake(self):
#         print('You step on the brakes')
#         return self
#
#     def turn_off(self):
#         print('You turn off the engine')
#         return self
#
# car = Car()
#
# car.turn_on().drive()
#
# car.brake().turn_off()
#
# car.turn_on()\
#     .drive()\
#     .brake()\
#     .turn_off()
######################################################################################################

    #SUPER FUNCTION
######################################################################################################
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
# class Square(Rectangle):
#     def __init__(self, length, width):
#         super().__init__(length,width)
#     def area(self):
#         return self.length*self.width
#
# class Cube(Rectangle):
#     def __init__(self, length, width, height):
#         super().__init__(length,width)
#         self.height = height
#     def volume(self):
#         return self.length*self.width*self.height
#
# square = Square(3, 3)
# cube = Cube(3, 3, 3)
#
# print(square.area())
# print(cube.volume())
######################################################################################################

    #ABSTRACTED CLASSES
######################################################################################################
# from abc import ABC, abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def go(self):
#         pass
#
#     @abstractmethod
#     def stop(self):
#         pass
#
# class Car(Vehicle):
#     def go(self):
#         print("You drive the car")
#
# class Motorcycle(Vehicle):
#     def go(self):
#         print("You ride the motorcycle")
#
# vehicle = Vehicle()
# car = Car()
# motorcycle = Motorcycle()
#
# vehicle.go()
# car.go()
# motorcycle.go()
######################################################################################################

    #OBJECTS AS ARGUMENTS
######################################################################################################
# class Car:
#     color = None
#
# class Motorcycle:
#     color = None
#
# def change_color(vehicle,color):
#     vehicle.color = color
#
# car_1 = Car()
# car_2 = Car()
# car_3 = Car()
#
# bike_1 = Motorcycle()
#
# change_color(car_1,'red')
# change_color(car_2,'white')
# change_color(car_3,'blue')
# change_color(bike_1,'black')
#
# print(car_1.color)
# print(car_2.color)
# print(car_3.color)
# print(bike_1.color)
######################################################################################################

    #DUCK TYPING
######################################################################################################
# class Duck:
#     def walk(self):
#         print('This duck is walking')
#
#     def talk(self):
#         print('This duck is qwuacking')
#
# class Chicken:
#     def walk(self):
#         print('This chicken is walking')
#
#     def talk(self):
#         print('This chicken  is clucking')
#
# class Person():
#     def catch(self,duck):
#         duck.walk()
#         duck.talk()
#         print('You caught the critter!')
#
# duck = Duck()
# chicken = Chicken()
# person = Person()
#
# person.catch(chicken)
######################################################################################################

    #WARLUS OPERATOR
######################################################################################################
# happy = True
# print(happy)
#
# print(happy := True)
#
# # foods = list()
# # while True:
# #     food = input('What food do you like?: ')
# #     if food == 'quit':
# #         break
# #     foods.append(foods)
#
# foods = list()
# while food := input('What food do you like') != 'quit':
#     foods.append(food)
# print(foods)
######################################################################################################

    #FUNCTIONS TO VARIABLES
######################################################################################################
# def hello():
#     print('Hello')
#
# hi = hello
# hello()
# hi()
#
# say = print
# say("Whoal. dammn")
######################################################################################################

    #HIGHER ORDER FUNCTIONS
######################################################################################################
# def loud(text):
#     return text.upper()
#
# def quit(text):
#     return text.lower()
#
# def hello(func):
#     text = func('Hello')
#     print(text)
#
# hello(loud)
# hello(quit)
#
# def divisor(x):
#     def divident(y):
#         return y / x
#     return divident
#
# divide = divisor(2)
# print(divide(10))
######################################################################################################

    #LAMBDA FUNCTION
######################################################################################################
# def bouble(x):
#     return x * 2
#
# print(bouble(5))
#
# double = lambda x: x*2
# multiply = lambda x,y: x * y
# add = lambda x,y,z: x + y + z
# full_name = lambda  first_name, last_name: first_name + " " +last_name
# age_check = lambda  age: True if age >= 18 else False
#
# print(age_check(17))
# print(full_name('Ihor', 'Sykuta'))
######################################################################################################

    #SORT
######################################################################################################
# students = ['Squidward', 'Sandy', 'Patrick', 'Spongebob', 'Mr.Krabs']
#
# students.sort(reverse=True)
#
# for i in students:
#     print(i, end=' ')
#
# students = ('Squidward', 'Sandy', 'Patrick', 'Spongebob', 'Mr.Krabs')
#
# sorted_students = sorted(students, reverse = True)
#
# for i in sorted_students:
#     print(i, end=' ')
#
# students = [("Squidward", 'F', 60),
#             ('Sandy', 'A', 33),
#             ('Patrick', 'D', 36),
#             ('Spongebob', 'B', 20),
#             ('Mr.Krabs', 'C', 78)]
# print('')
#
# age = lambda ages:ages[2]
# students.sort(key=age, reverse=True)
#
# for i in students:
#     print(i)
#
# students = [("Squidward", 'F', 60),
#             ('Sandy', 'A', 33),
#             ('Patrick', 'D', 36),
#             ('Spongebob', 'B', 20),
#             ('Mr.Krabs', 'C', 78)]
# age =  lambda  ages:ages[2]
# sorted_students = sorted(students, key=age)
#
# for i in sorted_students:
#     print(i, end='')
######################################################################################################

    #MAP
######################################################################################################
# store = [('shirt',20.00),
#          ('pants',25.00),
#          ('jackets',50.00),
#          ('socks',10.00)]
#
# to_euros = lambda data: (data[0], data[1]*0.82)
# to_dollars = lambda data: (data[0],data[1]/0.82)
# store_dollars = list(map(to_dollars,store))
# for i in store_dollars:
#     print(i)
######################################################################################################

    #FILTER
######################################################################################################
# friends = [('Rachel',19),
#            ('Monica',18),
#            ('Phoebe',17),
#            ('Joey',16),
#            ('Chandler',21),
#            ('Ross',20)]
#
# age = lambda data: data[1] >= 18
#
# drinking_buddies = list(filter(age, friends))
# for i in drinking_buddies:
#     print(i)
######################################################################################################

    #REDUCE
######################################################################################################
# import  functools
# letters = ['H', 'E', 'L', 'L', 'O']
# word = functools.reduce(lambda x, y: x+y,letters)
# print(word)
#
# factorial = [5,4,3,2,1]
# factorial_5 = functools.reduce(lambda num_1,num_2: num_1*num_2,factorial)
# print(factorial_5)
######################################################################################################

    #LIST COMPREHENSIONS
######################################################################################################
# squares = []
# for i in range(1,11):
#     squares.append(i*i)
# print(squares)
#
# squares = [i*i for i in range(1,11)]
# print(squares)
#
# students = [100,90,80,70,60,50,40,30,0]
# passed_student = list(filter(lambda mark: mark >=60, students))
# print(passed_student)
#
# passed_student_2 = [i if i >= 60 else 'failed' for i in students ]
# print(passed_student_2)
######################################################################################################

    #DICTIONARY COMPREHENSIONS
######################################################################################################
# cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
#
# cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
# print(cities_in_C)
# print(cities_in_F)
#
# weather = {'New York': 'snowing', 'Boston': 'sunny', 'Los Angeles': 'sunny', 'Chicago': 'cloudy'}
# sunny_wether = {key: value for (key, value) in weather.items() if value =='sunny'}
# print(sunny_wether)
#
# cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
#
# desc_cities = {key: 'Warm' if value >= 40 else 'Cold' for (key, value) in cities.items()}
# print(desc_cities)
#
#
# def check_temp(value):
#     if value >= 70:
#         return 'HOT'
#     elif 69 >= value >= 40:
#         return 'WARM'
#     else:
#         return 'COLD'
#
# cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# desc_cities = {key: check_temp(value) for (key, value) in cities.items()}
# print(desc_cities)
######################################################################################################

    #ZIP FUNCTION
######################################################################################################
# username = ['Dude', 'Bro', 'Mister']
# password = ('p@ssword', 'abc123', 'guest')
#
# users = dict(zip(username, password))
# print(type(users))
# for key, value in users.items():
#     print(key+ " : " + value)
#
# login_date = ['1/1/2021','1/2/2021','1/3/2021']
# users = zip(username, password, login_date)
#
# for i in users:
#     print(i)
######################################################################################################

    #IF _NAME_=='__MAIN__'
######################################################################################################
# import molule
#
# print(__name__)
# print(molule.__name__)
######################################################################################################

    #TIME MODULE
######################################################################################################
# import time
#
# print(time.time())
# print(time.ctime(time.time()))
# time_object = time.localtime()
# print(time_object)
# local_time = time.strftime('%B %d %Y %H:%M:%S',time_object)
# print(local_time)
# time_object = time.gmtime()
# print(time_object)
#
# time_string = '20 April, 2020'
# time_object = time.strptime(time_string, '%d %B, %Y')
# print(time_object)
#
# time_tuple = (2020, 4, 20, 4 ,20, 0 ,0, 0, 0)
# time_string = time.asctime()
# print(time_string)
######################################################################################################

    #THREADING
######################################################################################################
# import threading
# import time
#
# def eat_breakfast():
#     time.sleep(3)
#     print('You eat breakfast')
#
#
#
# def drink_coffee():
#     time.sleep(4)
#     print('You drink coffee')
#
# y = threading.Thread(target=drink_coffee, args=())
# y.start()
#
# def study():
#     time.sleep(5)
#     print('you finished studing')
#
# x = threading.Thread(target=eat_breakfast, args=())
# x.start()
#
# z = threading.Thread(target=study, args=())
# z.start()
#
# x.join()
# y.join()
# z.join()
#
# #eat_breakfast()
# #drink_coffee()
# #study()
#
# print(threading.active_count())
# print(threading.enumerate())
# print(time.perf_counter())
######################################################################################################

    #DAEMON THREADS
######################################################################################################
# import threading
# import time
#
# def timer():
#     print()
#     count = 0
#     while True:
#         time.sleep(1)
#         count += 1
#         print('Logged in for: ', count, 'seconds')
#
# x = threading.Thread(target=timer, daemon=True)
# x.start()
#
# answer = input('Do you wish to exit?')
######################################################################################################

    #Multiprocessing
######################################################################################################
# import multiprocessing
# import time
# def counter(num):
#     count = 0
#     while count < num:
#         count+=1
#
# def main():
#     a = multiprocessing.Procces(target=counter, args=(1000000000,))
#     a.start()
#
#     a.join()
#
#     print('Finished in:', time.perf_counter(),'seconds')
#
# if __name__ == '__main__':
#     main()
######################################################################################################

    #GUI windows
######################################################################################################
# from tkinter import *
#
# window = Tk()
# window.geometry('420x420')
# window.title('Mine first window')
# window.configure(bg='blue')
#
# window.mainloop()
#
# from tkinter import *
#
# gui = Tk(className='Python Examples - Window Color')
#
# # Set window size
# gui.geometry("400x200")
#
# # Set window color
# gui['bg']='green'
#
# gui.mainloop()
######################################################################################################

    #LABELS
######################################################################################################
# from tkinter import *
#
# window = Tk()
#
# label = Label(window,text='Hello World', font=('Arial', 40, 'bold'), fg='green')
# label.pack()
#
#
# window.mainloop()
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################




