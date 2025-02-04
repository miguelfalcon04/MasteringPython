# # If else
# print('IF ELSE')
# text = 'cd'

# if text == 'Hello':
#         print('Bot: Hello!')
# elif text == 'Bye':
#         print('Bot: Goodbye!')
# else:
#         print('I did not understand' )

# print('Succes') if 3 > 2 else print('failure')
# print()

# # For loop
# print('FOR LOOP')
# people: list[str] =['Mario', 'Luigi', 'Peach', 'Toad'] 

# for person in people:
#         print(f'Hello, {person}')

# for number in range(10):
#         print(number)

# print()

# # While Loop
# print('WHILE LOOP')

# a = 0
# while a < 10:
#         print(a)
#         a += 1

# print()

# # Break & continue
# print('BREAK & CONTINUE')

# for i in range(10):
#         print(i)
#         if i == 5:
#                 break

# i = 0
# while i<3:
#         print(i)
#         if i== 1:
#                 break

#         i += 1

# for i in range(5):
#         if i == 3:
#                 continue

#         print(i)

# print()

# # Pass 
# print('PASS')

# x , y = 10, 20
# if x > y:
#         pass

# print()

# # Loop Else
# print('LOOP ELSE')

# for i in range(5):
#         print(i, end=' ')

#         if i == 2:
#                 break
# else:
#         print('Succes')

# print()

# t = 0
# while t < 3:
#         print(t, end=' ')
#         t+=1

#         if t == 2:
#                 break
# else:
#         print('Succes')



# # # # # # # SECTION 5 FUNCTIONS # # # # # # # 
# def greet(name: str, greeting: str = 'Welcome', age: int = 0):
#         print(f'{greeting} {name}, {age}')
# greet('Juan', age=18)

# def do_something():
#         for i in range(3):
#                 print('Doing something')
#         print('Done')
# do_something()

# def sum_numbers(a : int, b : int) -> int:
#         return a + b

# print(type(sum_numbers(10,20)))

# def do_something(n:int):
#         print(n)
#         if n==1:
#                 print('Done')
#                 return
        
#         do_something(n - 1)

# do_something(3)

# def greet_people(*people: str, age):
#         print(people)
#         for name in people:
#                 print(f'Hello, {name}, {age}')

# greet_people('Mario', 'Luigi', 'Toad', age=10)

# def do_something(*args, **kwargs):
#         print(args)
#         print(kwargs)

#         print(kwargs['name'])

# do_something('Hello', name = 'Mario', age = 10)

# # # # # # # SECTION 6 ERROR HANDLING # # # # # # # 

# USER INPUT
# a = input('A: ')
# b = input('B: ')
# print(f'Sum: {int(a)+int(b)}')

# TRY...EXCEPT
# def do_math():
#     user_input = input('Enter a number: ')

#     try:
#         number = float(user_input)
#         # result = number / 0
#         print(number)
#     except ValueError:
#         print('Enter a valid number')
#         do_math()
#     # except ZeroDivisionError:
#     #     print('Please do not divide by 0')
#     except Exception as e:
#         print('Something went wrong', e)

# do_math()

# ELSE...FINALLY
# user_input: str = input('You: ')

# try:
#     number = float(user_input)
#     print(number)
# except Exception as e:
#     print('Exception:', e)
# else:
#     print('Succes')
# finally:
#     print('This will always run')

# RAISE
# user_input: str = input('You: ')
# if user_input == '0':
#     raise Exception('Please never use 0')

# is_connected: bool = False
# def connect_to_internet():
#     if not is_connected:
#         raise Exception('No Internet')
#     else:
#         print('Connected to internet')

# try:
#     connect_to_internet()
# except Exception as e:
#     print(e)

# # # # # # # SECTION 7 Packages & Modules # # # # # # # 

# IMPORTING MODULES
# import random
# print(random.randint(0,100))

# from sample_module import hello
# hello()

# IMPORTING PACKAGES
# from sample_package import sample_module, sample_module2

# sample_module.hello()
# sample_module2.hello2()

# INSTALLING EXTERNAL PACKAGES
# pip install requests
# import requests

# # # # # # # SECTION 8 Python Basics 2 # # # # # # # 
# file = open('sample.text')
# text = file.read()
# file.close()
# print(text)

# with open('sample.text') as file:
#     text = file.read()
#     print(text)

# import sample_module

# def hello():
#     print('hello')
#     sample_module.do_something()

# sample_module.do_something()

# ENUMS
# from enum import Enum

# class State(Enum):
#     OFF = 0
#     ON = 1

# state = State.ON
# if state == State.ON:
#     print('The lamp is turned on')
# elif state == State.OFF:
#     print('The lamp is turned off')


# class Color(Enum):
#     RED = 'Red'
#     BLUE = 'Blue'
#     GREEN = 'Green'

# c = Color.RED

# def check_color(color: Color):
#     if color == Color.RED:
#         print(color.value)
#     elif color == Color.GREEN:
#         print(color.name)
#     elif color == Color.BLUE:
#         print(color)

# check_color(c)

# COMPARING FLOATS
# a = 0.3
# b = 0.1 + 0.2
# print(a == b)

# def compare_float(a: float, b: float, tol: float) -> bool:
#     absolute = abs(a-b)
#     print(f'{a} - {b} = {a - b}')
#     return absolute < tol

# first = 0.8
# second = 0.1 + 0.7
# print(compare_float(first, second, tol=1e-10))

# if __name__ == '__main__':
# import sample_module
# print('Running code')

# NONLOCAL & GLOBAL

# x = 10

# def fun():
#     global x
#     x = 20
#     print('Inner: ', x)

# fun()
# print('Outer: ',x)

# def fun():
#     x = 20

#     def inner_fun():
#         nonlocal x
#         x = 10
#         print('Inner: ', x)

#     inner_fun()
#     print('Outer: ', x)

# fun()

# # # # # # # SECTION 9 Lists(Extended) # # # # # # # 
# LIST COMPREHENSIONS
# sample_list = []
# for i in range(10):
#     if i%2 == 0:
#         sample_list.append(i)
# print(sample_list)

# sample_list2 = [i for i in range(10) if i % 2 == 0]
# print(sample_list2)

# people: list[str] = ['Mario', 'Luigi', 'Peach']
# cap_people = [person.upper() for person in people]
# print(cap_people)

# SLICING LISTS WITH ::
# numbers: list[int] = list(range(21))
# print(numbers[::3])
# print(numbers[10::3])
# print(numbers[10:16:2])
# print(numbers[10:])
# print(numbers[:10])

# MODIFYING LISTS IN A LOOP
# people: list[str] = ['Mario', 'Luigi', 'Peach', 'Toads']
# people2: list[str] = []

# for person in people:
#     print(person, ' -> ', people2)

#     if person == 'Luigi':
#         pass
#     else:
#         people2.append(person)

#     if person == 'Peach':
#         print('Hi I am Peach')

# print(people2)

# # # # # # # SECTION 10 OOP # # # # # # # 

# CLASSES & OBJECTS
# class Lamp:
#     def __init__(self, model: str, color: str):
#         self.model = model
#         self.color = color
    
#     def turn_on(self):
#         print(self.model, 'is turned on')
    
#     def turn_off(self):
#         print(self.model, 'is turned off')
    
#     def describe(self):
#         print(f'Lamp: {self.model} ({self.color})')
        
# red_lamp: Lamp = Lamp('SmallLamp', 'Red')
# red_lamp.turn_on()
# red_lamp.turn_off()
# red_lamp.color = 'Blue'
# red_lamp.describe()

# green_lamp: Lamp = Lamp('BigLamp', 'Green')
# green_lamp.turn_on()

# CLASS VARIABLES & INSTANCE VARIABLES
# class Animal:
#     tricks: list[str] = []
    
#     def __init__(self, name:str):
#         self.name = name
    
#     def teach_trick(self, trick_name: str):
#         self.tricks.append(trick_name)
        
# if __name__ == '__main__':
#     dog: Animal = Animal('Dog')
#     cat: Animal = Animal('Cat')
#     dog.teach_trick('Make dinner')
#     dog.teach_trick('Go to work')
    
#     print('Dog tricks: ', dog.tricks)
#     print('Cat tricks: ', cat.tricks)

# GETTERS & SETTERS

# class Fruit:
#     def __init__(self, name: str):
#         self._name = name
    
#     @property
#     def name(self):
#         print(f'{self._name} is being accesed')
#         return self._name
    
#     @name.setter
#     def name(self, value: str):
#         print(f'{self._name} is now: {value}')
#         self._name = value

# if __name__ == '__main__':
#     apple: Fruit = Fruit('Apple')
#     apple.name
#     apple.name = 'Banana'
#     print(apple.name)

# __INIT__() __STR__() __REPR__() __EQ__()
# class Car:
#     def __init__(self, model: str, color: str):
#         self.model = model
#         self.color = color
    
#     def drive(self):
#         print(f'{self.model} is now driving')
    
#     def explode(self):
#         print(f'{self.name}, exploded')
#     def __str__(self):
#         return f'{self.model} ({self.color})'
    
#     def __repr__(self):
#         return f'Car(model={self.model}, color={self.color})'
    
#     def __eq__(self, value):
#         return self.__dict__ == value.__dict__


# if __name__ == '__main__':
#     car: Car = Car('BMW', 'Blue')
#     car2: Car = Car('BMW', 'Blue')
#     car.drive()
#     print(car)
#     print(car.__repr__())
#     print(car == car2)
    
#     def hello():
#         print('Hello')

# PRIVATE & PROTECTED
# class Lamp:
#     def __init__(self, name: str, model: int, version: int):
#         self.name = name
#         self.__model = model
#         self._version = version
    
#     def description(self):
#         self.__self_maintenance()
#         print(self.name, self.__model)
    
#     def __self_maintenance(self):
#         print(self.name,'is fixing itself')

# class ElectricLamp(Lamp):
#     def __init__(self, name: str, model: int, version: int):
#         super().__init__(name, model, version)
    
#     def do_something(self):
#         print(self._version)

# lamp: Lamp = Lamp('Lamp', 1010, 12345)
# lamp.description()

# electric_lamp: ElectricLamp = ElectricLamp('El lamp', 1010, 1234)
# electric_lamp.do_something()

# INHERITANCE
# class Animal:
#     def __init__(self, name: str,):
#         self.name = name
    
#     def eat(self):
#         print(f'{self.name} is eating')
    
#     def sleep(self):
#         print(f'{self.name} is sleeping')

# class Cat(Animal):
#     def __init__(self, name: str, weight: float):
#         super().__init__(name)
#         self.weight = weight
    
#     def meow(self):
#         print(f'{self.name} says meow')

# cat: Cat = Cat('Garflied', 100)
# cat.meow()
# cat.sleep()

# SUPER
# class Lamp:
#     def __init__(self, model: str):
#         self.model = model
    
#     def turn_on(self):
#         print(self.model, 'is turned on')
    
#     def turn_off(self):
#         print(self.model, 'is turned off')

# class ElectricLamp(Lamp):
#     def __init__(self, model):
#         super().__init__(model)
    
#     def turn_on(self):
#         print('Using electricity')
#         super().turn_on()

# el_lamp = ElectricLamp = ElectricLamp('Bicho')
# el_lamp.turn_on()

# @CLASSMETHOD @STATICMETHOD
# class Calculator:
#     def __init__(self, name: str):
#         self.name = name
    
#     def description(self):
#         print(f'{self.name} is a calcultor')
    
#     @staticmethod
#     def add_numbers(a: float, b: float):
#         print(a+b)
    
#     @classmethod
#     def create_with_version(cls, name: str, version: int):
#         return cls(f'{name}: ({version})')

# calc: Calculator = Calculator.create_with_version('Pepe', 2)
# calc.description()
# calc.add_numbers(1,2)
# Calculator.add_numbers(10,20)

# @ABSTRACTMETHOD
# from abc import ABC, abstractmethod

# class Phone(ABC):
#     def __init__(self, model: str):
#         self.model = model
    
#     @property
#     @abstractmethod
#     def power(self):
#         ...
    
#     @abstractmethod
#     def call_target(self, person: str):
#         ...

# class iBanana(Phone):
#     def __init__(self, model: str):
#         super().__init__(model)
    
#     @property
#     def power(self):
#         raise NotImplementedError('Code Missing...')
    
#     def call_target(self, person: str):
#         pass


# phone = iBanana('iBanana')
# phone.power()

# PROTOCOLS
# from typing import Protocol

# class Printable(Protocol):
#     pages: int
    
#     def print(self):
#         pass
    
#     def recycle(self):
#         pass

# class Book:
#     pages: int
    
#     def __init__(self, title: str):
#         self.title = title
    
#     def print(self):
#         print('Printing book:', self.title)
    
#     def recycle(self):
#         print('Recycling book:', self.title)

# class Magazine:
#     pages: int
    
#     def __init__(self, title: str):
#         self.title = title
    
#     def print(self):
#         print('Printing magazine:', self.title)
    
#     def recycle(self):
#         print('Recycling magazine:', self.title)

# def print_item(printable: Printable):
#     printable.print()

# book: Printable = Book('Python')
# print_item(book)

# magazine: Printable = Magazine('Deluxe')
# print_item(magazine)

# __INIT__ VS __NEW__
# class Connection:
#     __instance = None
    
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             print('Connecting...')
#             cls.__instance = super().__new__(cls)
#             return cls.__instance
#         else:
#             print('WARNING: There is already a connection')
#             return cls.__instance
    
#     def __init__(self):
#         print('Connected to Internet')

# connection = Connection()
# connection2 = Connection()
# print(connection == connection2)

# # # # # # # SECTION 11 BUILT IN FUNCTIONS # # # # # # # 

# PRINT
# print('This a test', 10, 'Hello', sep=' - ', end='Se acabó')

# ENUMERATE
# names: list[str] = ['Mario', 'Luigi', 'Peach', 'Toad']
# for name in names:
#     print(names.index(name),':',name)

# for i, name in enumerate(names):
#     print(i, ':', name)

# ROUND
# number: float = 1.6666
# print(round(number, 2))

# RANGE
# numbers: range = range(0, -10, -1)
# print(list(numbers))

# GLOBALS & LOCALS
# var: str = 'GLOBAL'

# def hello():
#     return 'GLOBAL'

# def bye():
#     bye_str: str = 'str'
#     bye_int: int = 0
    
#     def inner():
#         pass
    
#     print(locals())

# print(globals())

# ALL() & ANY()
# is_connected: bool = True
# has_electricity: bool = False
# has_paid: bool = True

# requirements: list[bool] = [is_connected, has_electricity, has_paid]

# has_internet: bool = all(requirements)
# has_internet2: bool = any(requirements)
# print('Internet:', has_internet)
# print('Internet:', has_internet2)

# ISINSTANCE()
# class Fruit:
#     def __init__(self, name: str):
#         self.name = name

# apple: Fruit = Fruit('Apple')

# print(isinstance(apple, Fruit))
# print(isinstance(apple, str))

# CALLABLE()
# a: str = 'a'

# def do_something():
#     pass

# def b():
#     pass

# print(callable(a))
# print(callable(do_something))
# print(callable(b))

# FILTER()
# people:list [str, int] = ['mario', 'luigi', 10, 'Toas', 20]

# def is_str(element):
#     return isinstance(element,str)

# filtered_people: list[str] = list(filter(is_str, people))
# print(filtered_people)

# MAP()
# numbers: list[int] = [1,2,3,4,5,6]

# def convert_to_str(element):
#     return str(element)

# converted_list: list[str] = list(map(convert_to_str, numbers))
# print(converted_list)

# SORTED()
# numbers: list[int] = [1, 6, 4, 5, 3, 2, 9, 8]
# sorted_numbers: list[int] = sorted(numbers, reverse=True)

# print(sorted_numbers)

# EVAL()
# user_input: str = input('Insert your maths: ')
# result: float = eval(user_input)
# print(result)

# EXEC()
# user_input: str = input('Your code: ')
# exec(user_input)

# ZIP()
# people = ('mario', 'Luigi', 'Toad')
# numbers = (10, 20, 30)
# letters = ('a', 'b', 'c')

# zipped = zip(people, numbers, letters)

# for item in zipped:
#     print(item)

# # # # # # # SECTION 12 PYTHON ADVANCED # # # # # # # 

# # "IS" VS "=="
# class Fruit:
#     def __init__(self, name: str, calories: float):
#         self.name = name,
#         self.calories = calories
    
#     def __eq__(self, value):
#         return self.__dict__ == value.__dict__

# fruit_a: Fruit = Fruit('Banana', 10)
# fruit_b: Fruit = Fruit('Banana', 10)

# print(f'fruit_a is fruit_b = {fruit_a is fruit_b}')
# print(f'fruit_a == fruit_b = {fruit_a == fruit_b}')

# # LAMBDA FUNCTIONS
# def square(a: float) -> float:
#     return a ** 2

# sq = lambda a: a ** 2

# print(square(4))
# print(sq(4))

# numbers: list[int] = [1,2,3,4,5,6,7]
# even: list[int] = list(filter(lambda a: a % 2 == 0, numbers))
# print(even)

# # WALRUS OPERATOR

# def get_info(text: str) -> dict:
#     return{'text:': text,
#             'letters': (length := len(text.replace(' ', ''))),
#             'words': (words := text.split()),
#             'total_words': (word_length := len(words)),
#             'avg_per_word': round(length / word_length, 2)}

# for key, value, in get_info('This is some text').items():
#     print(key, value, sep=': ')

# while user_input := input('You: '):
#     print('>>', user_input)
# else:
#     print('We are done here')

# # DATACLASSES
# from dataclasses import dataclass

# @dataclass
# class Fruit2:
#     name: str
#     calories: float

# class Fruit:
#     def __init__(self, name: str, calories: float):
#         self.name = name,
#         self.calories = calories
    
#     def __eq__(self, value):
#         self.__dict__ == value.__dict__

# apple: Fruit = Fruit('apple',10)
# apple2: Fruit2 = Fruit2('apple',10)
# print(apple == apple2)

# # GENERATORS

# def generate_list(n: int):
#     for i in range(n):
#         yield i

# generator = generate_list(100)

# list_a: list[int] = []
# for number in generator:
#     list_a.append(number)
    
#     if number == 10:
#         break

# print(list_a)
# print(next(generator))

# yield_comprehension = (i for i in range(10*100))
# print(next(yield_comprehension))
# print(next(yield_comprehension))
# print(next(yield_comprehension))
# print(next(yield_comprehension))

# # DELETE
# people: list[str] = ['Mario', 'Toad']
# del people[1]
# print(people)

# data: dict = {
#     'field1': 100,
#     'field2': 200
# }
# del data['field2']
# print(data)

# name: str = 'Mario'
# del name

# from dataclasses import dataclass
# @dataclass
# class Fruit:
#     name: str
#     calories: float

# apple: Fruit = Fruit('apple', 10)
# print(apple)

# del apple

# print(apple)

# # ASSERT

# def start_program(data: dict):
#     assert isinstance(data, dict), 'Invalid JSON'
#     assert data, 'No data found...'
#     print('Program loaded successfully')

# json: dict = {'name':'mario'}
# start_program(data=json)

# # MATCH-CASE
# status: int = 405

# if status == 400:
#     print('Bad request')
# elif status == 403:
#     print('Forbidden request')
# elif status == 404:
#     print('Not found...')
# else:
#     print('Something went wrong...')


# match status:
#     case 400:
#         print('Bad request')
#     case 403:
#         print('Forbidden request')
#     case 404:
#         print('Not found...')
#     case _:
#         print('Something went wrong...')


# user_input: str = input('command: ')
# p_command: list[str] = user_input.split()

# match p_command:
#     case ['find', *images]:
#         print(f'Finding: {images}')
#     case ['download', *images]:
#         print(f'Downloading: {images}')
#     case ['cancel' | 'delete', *images] if len(images) > 1:
#         print(f'Deleting: {images}')


# # DECORATORS

# from functools import wraps
# from time import perf_counter, sleep
# from typing import Callable

# def get_time(func):
#     """Times any function"""
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start_time: float = perf_counter()
#         func(*args, **kwargs)
#         end_time: float = perf_counter()
        
#         total_time: float = round(end_time -start_time, 3)
#         print('Time: ', total_time, 'seconds')
#     return wrapper

# @get_time
# def do_something(param):
#     """Do something important"""
#     sleep(1)
#     print(param)
#     for i in range(10**8):
#         pass

# do_something('Hello')

# def repeat(times: int):
#     """Repeat function call x amount of times"""
    
#     def decorator(func: Callable):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             value = None
#             for _ in range(times):
#                 value = func(*args, **kwargs)
            
#             return value
#         return wrapper
#     return decorator

# @repeat(5)
# def func1():
#     print('Hello')

# func1()

# # MEMOIZATION
# from functools import wraps
# from time import perf_counter
# import sys

# def memoize(func):
#     cache: dict = {}
    
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         key: str = str(args)+ str(kwargs)
        
#         if key not in cache:
#             cache[key] = func(*args, **kwargs)
#         return cache[key]
#     return wrapper


# @memoize
# def fibonacci(n) -> int:
#     if n < 2:
#         return n
#     return fibonacci(n -1) + fibonacci(n - 2)

# sys.setrecursionlimit(10_000)
# start: float = perf_counter()
# f: int = fibonacci(1000)
# end: float = perf_counter()
# print(f)
# print(f'Time: {end - start}')

# # CONTEXT MANAGERS
# class File:
#     def __init__(self, name: str):
#         self.name = name
    
#     def __enter__(self):
#         print(f'Opnening {self.name}...')
#         return self
    
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(f'Closing {self.name}')

# with File('main.py') as file:
#     print(file.name)


# # TIMING CODE PERFORMANCE
# import time
# import timeit

# def time_func(func):
#     start_time: float = time.perf_counter()

#     for i in range(10**3):
#         pass

#     print('Hello')
#     time.sleep(1)

#     end_time: float = time.perf_counter()

#     print(f'Total time:', end_time-start_time, 'seconds')

# def make_calculation(first: int, second: int):
#     for i in range(10**3):
#         pass
#     return first + second

# def do_something():
#     for i in range(10):
#         x: int = i ** i


# def get_time(func: str, repeat: int, number: int) -> float:
#     speed: float = min(timeit.repeat(func, repeat=repeat, number=number, globals=globals()))
#     print(f'{func} --> {round(speed, 4)} seconds (ran {repeat * number:,} times)')
#     return speed

# a, b = 1, 2
# get_time('do_something()', repeat=10, number=10**5)
# get_time('make_calculation(a, b)', repeat=10, number=10**2)

# # MONKEY PATCHING

# import requests

# def get(url: str):
#     return '<TEST_RESPONSE>'

# requests.get = get

# data = requests.get('https://www.apple.com')
# print(data)

# # CUSTOM EXCEPTIONS

# class NegativeException(Exception):
#     """Raise if a value is below 0"""
#     def __init__(self, number: float, error_code: int):
#         self.number = number
#         self.error_code = error_code
#         super().__init__(f'{self.number} is less than 0 (ERROR_CODE: {self.error_code})', self.number, self.error_code)
    
#     def __str__(self):
#         return f'{self.number} is less than 0 (ERROR_CODE: {self.error_code})'
    
#     def custom_method(self):
#         print((self.number, self.error_code), 'were used by the custom method')
    
#     def __reduce__(self):
#         return NegativeException, (self.number, self.error_code)
# try:
#     raise NegativeException(-5, 999)
# except NegativeException as e:
#     print(e)
#     print(e.args)
#     e.custom_method()


# # # # # # # SECTION 14 File Management # # # # # # # 

# # READING FILES

# with open('sample.text', 'r') as text:
#     t : list[str] = text.readlines()
#     print(text.readline())
#     print(text.read())
#     print(t)


# # WRITING & CREATING FILES
# with open('sample.text', 'a+') as text:
#     text.write('\n1234')
#     text.seek(0)
#     print(text.read())

# # Reemplaza todo el archivo
# with open('sample.text', 'w+') as text:
#     text.write('\n1234')
#     text.seek(0)
#     print(text.read())

# # Crea el archivo si no existe. Si existe da un error
# with open('hello.text', 'x+') as text:
#     text.write('\n1234')
#     text.seek(0)
#     print(text.read())

# # DELETING FILES
# import os

# if os.path.exists('hello.text'):
    # os.remove('hello.text')

# for item in os.listdir('sample_folder'):
#     if os.path.exists('sample_folder/' + item):
#         os.remove('sample_folder/' + item)

# os.rmdir('sample_folder')

# # HANDLING JSON
# import json

# def get_json(file: str) -> dict:
#     with open(file, 'r') as file:
#         data: str = file.read()
#         actual: dict = json.loads(data)
#         return actual

# sample_data: dict = get_json('data.json') 
# print(sample_data)

# sample: dict = {'name': 'Elon', 'age': 12, 'has_mars': False}
# sample_json = json.dumps(sample)
# print(sample_json)

# with open('sample.json', 'w') as file:
#     json.dump(sample, file)

# # CACHING JSON
# import json
# import requests

# def fech_data(*, update: bool= False, json_cache: str, url: str) -> dict:
#     if update:
#         json_data = None
#     else:
#         try:
#             with open(json_cache, 'r') as file:
#                 json_data = json.load(file)
#                 print('Fetched data from the local cache!')

#         except(FileNotFoundError, json.JSONDecodeError) as e:
#             print(f'No local cache found ({e})')
#             json_data = None
    
#     if not json_data:
#         print('Fetching new json data... (Creating local cache)')
#         json_data = requests.get(url).json()
#         with open(json_cache, 'w') as file:
#             json.dump(json_data, file)
#     return json_data

# api_url: str = 'https://dummyjson.com/comments'
# cache_file: str = 'comments.json'

# data: dict = fech_data(
#     update= False,
#     json_cache=cache_file,
#     url=api_url
# )
# print(data)

# # GLOB
# import glob

# # ? matches any single character
# print(glob.glob('?ata.json'))

# # * matches everything
# print(glob.glob('*.json'))

# # The first letter must be a or d or c
# print(glob.glob('[sdc]*'))

# # The first letter must not be a or d or c
# print(glob.glob('[!sdc]*'))

# print(glob.glob('**/*.js', 
#                 root_dir='/Users/falco/PythonUdemy',
#                 recursive=True,
#                 include_hidden=True))

# globs = glob.iglob('**/*.py', 
#                 root_dir='/Users/falco/PythonUdemy',
#                 recursive=True,
#                 include_hidden=True)

# for i, file in enumerate(globs):
#     print(i, file, sep=':')


# # PICKLING
# import pickle

# text: str = 'text'
# number: int = 10

# with open('save.txt', 'w') as file:
#     file.write(text + '\n')
#     file.write(str(number) + '\n')

# with open('save.txt', 'r') as file:
#     print(file.read())

# class Fruit:
#     def __init__(self, name: str, calories: float):
#         self.name = name
#         self.calories = calories
#     def describe_fruit(self):
#         print(self.name, ':', self.calories)

# with open('save_pickle.txt', 'rb') as file:
#     fruit: Fruit = pickle.load(file)

# print(fruit.describe_fruit())

# # # # # # # SECTION 15 AsyncIO # # # # # # # 
# import asyncio

# async def fetch_data(data: int) -> dict:
#     print('Fetching data...')
#     await asyncio.sleep(2)
#     return {'data': data}

# async def counter():
#     for i in range(10):
#         await asyncio.sleep(0.5)
#         print(i)

# async def main():
#     task1 = asyncio.create_task(fetch_data(123))
#     task2 = asyncio.create_task(counter())
    
#     data: dict = await task1
#     print(data)
#     await task2

# asyncio.run(main())

# # TASKS
# import asyncio

# async def fetch_data(data: int) -> dict:
#     print('Fetching data...')
#     await asyncio.sleep(6)
#     return {'data': data}

# async def main():
#     task = asyncio.create_task(fetch_data(100))
#     await asyncio.sleep(4)
    
#     # task.cancel()
#     # await asyncio.sleep(0.1)
#     # print(task.cancelled())
#     try:
#         await asyncio.wait_for(task, timeout=5)
        
#         if task.done():
#             data: dict = task.result()
#             print(data)
#         else:
#             print('Data not ready')
#     except asyncio.CancelledError:
#         print('task was cancelled')

# asyncio.run(main())

# # GATHER
# import asyncio

# async def fetch_data(data: int) -> dict:
#     print('Fetching data...')
#     await asyncio.sleep(1)
    
#     if data == 0:
#         raise Exception('No data')
#     return {'data': data}

# async def main():
#     tasks = asyncio.gather(
#         fetch_data(1),
#         fetch_data(2),
#         fetch_data(3),
#         fetch_data(0),
#         return_exceptions=True
#     )
#     results = await tasks
#     print(results)

# asyncio.run(main())

# # SLEEP
# import asyncio

# async def counter(e):
#     print('starting task')
#     for i in range(e):
#         print(i)
#         if i % 10_000 == 0:
#             await asyncio.sleep(0)

# async def main():
#     print('Started')
#     task = asyncio.create_task(counter(100_000_000))
#     await asyncio.sleep(1)
#     task.cancel()

# asyncio.run(main())

# # # # # # # SECTION 16 MULTITHREADING # # # # # # # 

# # THREADS
# import threading
# import time

# def process_data(name:str, count: int):
#     print(f'Starting {name}....')
    
#     for i in range(count):
#         print(name, i + 1, sep=': ')
#         time.sleep(1)

# thread_one = threading.Thread(target=process_data, args=('Thread1', 10))
# thread_two = threading.Thread(target=process_data, args=('Thread2', 5))

# thread_one.start()
# time.sleep(1)
# thread_two.start()

# # LOCKS

# lock = threading.Lock()
# def counter(limit: int, name: str):
#     for i in range(limit):
#         time.sleep(0.5)
#         print(name, i+1, sep=': ')

# def task1():
#     lock.acquire()
#     counter(5, 'T-1')
#     lock.release()

# def task2():
#     lock.acquire() # If lock is being used in another place until it is not release it wont start 
#     counter(5, 'T-2')
#     lock.release()

# def task3():
#     counter(5, 'T-3')

# def main():
#     thread = threading.Thread(target=task1)
#     thread2 = threading.Thread(target=task2) 
#     thread3 = threading.Thread(target=task3) 
    
    # thread.start()
    # thread2.start()
    # thread3.start()

# main()

# # DAEMON THREADS

# def infinite_loop():
#     while True:
#         print(time.time())
#         time.sleep(1)

# thread_infinite = threading.Thread(target=infinite_loop, daemon=True) #Just a low priority thread that can be shutted down by other threads
# thread_infinite.start()

# # SEMAPHORES Create a limit of how many locks can be used
# # WITH LOCK / SEMAPHORE

# import threading
# import time

# sem = threading.Semaphore(5)

# def process_something(id: int):
#     # sem.acquire()
#     # print(f'{id} --> Running')
#     # time.sleep(5)
#     # print(f'{id} --> Finished')
#     # sem.release()
    
#     # # The same. It opens and release automatically
#     with sem:
#         print(f'{id} --> Running')
#         time.sleep(5)
#         print(f'{id} --> Finished')

# for i in range(10):
#     time.sleep(0.5)
#     thread = threading.Thread(target=process_something, kwargs={'id': i + 1})
#     thread.start()


# # RACE CONDITIONS

# lock = threading.Lock()

# def edit(operation: str, amount: int, repeat: int):
#     global value
    
#     lock.acquire()
#     for _ in range(repeat):
#         temp: int = value
#         time.sleep(0)
#         if operation == 'add':
#             temp += amount
#         elif operation == 'subtract':
#             temp -= amount
        
#         time.sleep(0)
#         value = temp
    
#     lock.release()

# value: int = 0
# adder = threading.Thread(target=edit, args=('add', 100, 100_000))
# subtarctor = threading.Thread(target=edit, args=('subtract', 100, 100_000))

# adder.start()
# subtarctor.start()

# print('Waiting for threads to finish...')

# adder.join()
# subtarctor.join()

# print(f'{value = }')

# # # # # # # SECTION 17 MULTIPROCESSING # # # # # # # 

# # PROCESSES
# import multiprocessing as mp
# from time_stuff import get_time, timestamp, kill_time
# import os

# def func(param):
#     print(f'Starting {mp.current_process().name} ({os.getpid()})... ({timestamp()})')
#     kill_time()
#     print(f'{os.getpid()} finished ({timestamp()})')

# @get_time
# def main():
#     process = mp.Process(name='Process-1', target=func, args=('Sample',))
#     process2 = mp.Process(name='Process-2', target=func, args=('Sample2',))
    
#     process.start()
#     process2.start()
    
#     process.join()
#     process2.join()

# if __name__ == '__main__':
#     main()

# # POOLS (MAP) Codigo para mostrar como funciona el multiprocessing con los cores. 
# import multiprocessing as mp
# from time_stuff import get_time, kill_time
# import time

# def convert_to_x(number: int) -> str:
#     time.sleep(2)
#     return number * 'x'

# @get_time
# def main():
#     print(f'Cores avaliable: {mp.cpu_count()}')
    
#     values: tuple[int, ...] = tuple(range(1, 10))
    
#     # Solo tomará 4 cores, hasta que no se liberen no seguirá con el resto
#     with mp.Pool(processes=4) as pool:
#         results: list[str] = pool.map(convert_to_x, values)
#         print('Results:', results)

# if __name__ == '__main__':
#     main()

# # POOLS (STARMAP) Se usa para pasar multiples argumentos en las funciones
# import multiprocessing as mp
# from time_stuff import get_time
# import time

# def add_numbers(*args) -> float:
#     time.sleep(2)
#     return(sum(args))

# @get_time
# def main():
#     print(f'Cores avaliable: {mp.cpu_count()}')
    
#     values = ((1,2,10), (3,4), (5,6), (7,8,111))
    
#     with mp.Pool() as pool:
#         results: list[float] = pool.starmap(add_numbers, values)
#         print('Results:', results)

# if __name__ == '__main__':
#     main()

# # POOLS (MULTIPLE FUNCTIONS)
# import multiprocessing as mp
# from time_stuff import get_time
# import functools
# import time

# def func_a(param):
#     time.sleep(2)
#     return param

# def func_b(param):
#     time.sleep(2)
#     return param

# def func_c(param, param2):
#     time.sleep(2)
#     return param, param2

# def map_func(func):
#     return func()

# @get_time
# def main():
#     print(f'Cores avaliable: {mp.cpu_count()}')
    
#     a = functools.partial(func_a, 'A')
#     b = functools.partial(func_b, 'B')
#     c = functools.partial(func_c, 'C', 'C2')
    
#     with mp.Pool() as pool:
#         results = pool.map(map_func, [a, b, c])
#         print(results)


# if __name__ == '__main__':
#     main()


# # DATA SHARING ISSUE // While multiprocessing each core has its own copy of data so will be conflicts at the return
# from multiprocessing import Process

# numbers: list[int] = [0]

# def func():
#     global numbers
    
#     numbers.extend([1, 2, 3])
#     print(f'Process data: {numbers}')

# def main():
#     process = Process(target=func)
#     process.start()
#     process.join()
#     print('Main data:', numbers)

# if __name__ == '__main__':
#     main()

# # PIPES 
# from multiprocessing import Pipe, Process, current_process
# from random import randint
# import os
# import time

# def sender(connection):
#     print(f'Sender: {current_process().name} ({os.getpid()})...')
    
#     for _ in range(5):
#         rand: int = randint(1, 10)
#         connection.send(rand)
#         print(f'{rand} was sent...')
#         time.sleep(0.5)
#     print('Sending "None"...')
#     connection.send(None)
#     print('Done with sending data')

# def reciver(connection):
#     print(f'Reciever: {current_process().name} ({os.getpid()})...')
    
#     while True:
#         data = connection.recv()
#         print(f'{data} was recieved...')
        
#         if data is None:
#             break
#     print('Done with recieving data')

# def main():
#     c1, c2 = Pipe()
    
#     sender_process = Process(target=sender, args=(c2,))
#     receiver_process = Process(target=reciver, args=(c1,))
    
#     sender_process.start()
#     receiver_process.start()
    
#     sender_process.join()
#     receiver_process.join()

# if __name__ == '__main__':
#     main()


# # QUEUES
# from multiprocessing import Process, Queue, current_process
# import time

# def insert_val(queue: Queue, i: int):
#     print(f'{i} was put in the queue...')
#     queue.put(i)

# def func(queue: Queue):
#     name: str = current_process().name
    
#     try:
#         print(f'{name} received data: {queue.get(timeout=3)}')
#     except Exception as e:
#         print('Timeout!', e)

# def square_number(identifier: int, num: int, queue: Queue):
#     time.sleep(2)
#     queue.put((identifier, num ** 2))

# def main():
#     queue: Queue = Queue()
#     data: list[int] = list(range(1, 9))
    
#     processes = [Process(target=square_number, args=(identifier, num, queue))
#                 for identifier, num in enumerate(data)]
    
#     for process in processes:
#         process.start()
    
#     for process in processes:
#         process.join()
    
#     unsorted = [queue.get() for _ in processes]
#     print(unsorted)
    
#     result = [val[1] for val in sorted(unsorted)]
#     print(result)


# def main():
#     queue: Queue = Queue()
#     queue.put(1)
#     # queue.put(2)
#     queue.put(3)
#     # queue.put(4)
    
#     processes = [Process(target=func, args=(queue,)) for _ in range(4)]
    
#     for process in processes:
#         process.start()
    
#     for process in processes:
#         process.join()


# def main():
#     queue: Queue = Queue()
    
#     processes = [Process(target=insert_val, args=(queue, i)) for i in range(5)]
    
#     for process in processes:
#         process.start()
    
#     for process in processes:
#         process.join()
    
#     results = [queue.get() for _ in processes]
#     print(results)

# if __name__ == '__main__':
#     main()

# # LOCKS & SEMAPHORES
# from time import sleep
# from multiprocessing import Process, Lock, Semaphore

# def func(p_lock, identifier):
    
#     with p_lock:
#         sleep(1)
#         print(f'>> Process {identifier} is running')

# def main():
#     lock = Lock()
#     sem = Semaphore(3)
    
#     processes = [Process(target=func, args=(lock, i)) for i in range(5)]
    
#     for process in processes:
#         process.start()
    
#     for process in processes:
#         process.join()

# if __name__ == '__main__':
#     main()


# # # # # # # SECTION 19 Projects # # # # # # # 


# # # # # # # IMPOSSIBLE QUIZ # # # # # # # 
# import time
# from dataclasses import dataclass
# from random import choice, shuffle

# @dataclass(slots=True)
# class Question:
#     question: str
#     answers: list[str]
#     correct_answer: str

# def random_question(questions: list[Question]) -> int:
#     question: Question = choice(questions)
#     print(f'{question.question}')
    
#     shuffle(question.answers)
    
#     for answer in question.answers:
#         print('-', answer)
    
#     user_input: str = input('\nYour answer >> ').lower().strip()
    
#     if user_input == question.correct_answer:
#         print('Correct\n')
#         questions.remove(question)
#         return 1
#     else:
#         print(f'Wrong, the answer was: {question.correct_answer.capitalize()}\n')
#         questions.remove(question)
#         return 0

# def run_quiz(questions: list[Question]):
#     total_score: int = 0
#     while questions:
#         score: int = random_question(questions=questions)
#         total_score += score
#         time.sleep(2)
#     else:
#         print('Final score:', total_score)

# def get_questions() -> list[Question]:
#     return [
#         Question(question='How are you?',
#                 answers=['Good', 'Bad', 'Ok', 'Potato'],
#                 correct_answer='good'),
#         Question(question='What is your name?',
#                 answers=['Mario', 'Luigi', 'Peach', 'Miguel'],
#                 correct_answer='miguel'),
#         Question(question='What time is it?',
#                 answers=['10', '11', '12', '13s'],
#                 correct_answer='10'),
#     ]

# def main():
#     questions: list[Question] = get_questions()
#     run_quiz(questions=questions)

# if __name__ == '__main__':
#     main()

# # # # # # # MY OWN API # # # # # # # 

# from flask import Flask, request
# from collections import namedtuple
# from datetime import date
# from time import time

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return {'Test': 'This is an example',
#             'Time': date.today(),
#             'Timestamp': time()}

# @app.route('/chat')
# def chat():
#     user_input: str = request.args.get('input')
#     response: Response = generate_responses(user_input)
    
#     json = {
#         'input': user_input,
#         'response': response.response,
#         'accuracy': response.accuracy
#     }
    
#     return json

# Response = namedtuple('Response', 'response accuracy')

# def generate_responses(user_input: str) -> Response :
#     lc_input: str = user_input.lower()
    
#     if lc_input == 'hello':
#         return Response('Hey there', 1)
#     elif lc_input == 'goodbye':
#         return Response('See you later', 1)
#     else:
#         return Response('Could not understand', 0)
    

# if __name__ == '__main__':
#     app.run()

# # # # # # # ACCURATE CHAT BOT # # # # # # # 

# import json
# import re
# import random_responses

# def load_json(file):
#     with open(file) as bot_responses:
#         print(f'Loaded "{file}" succesfully!')
#         return json.load(bot_responses)
    

# response_data: dict = load_json('responses.json')

# def get_response(input_str: str):
#     split_message: list[str] = re.split(r'\s+|[,;?!.-]\s*', input_str.lower())
#     score_list: list[int] = []
    
#     for response in response_data:
#         required_score: int = 0
#         response_score: int = 0
#         required_words: list[str] = response['required_words']
        
#         if required_words:
#             for word in split_message:
#                 if word in required_words:
#                     required_score += 1
        
#         if required_score == len(required_words):
#             for word in split_message:
#                 if word in response['user_input']:
#                     response_score += 1
            
#         score_list.append(response_score)
    
#     best_response: int = max(score_list)
#     response_index: int = score_list.index(best_response)
    
#     if input_str == "":
#         return "Please type somethin"
    
#     if best_response != 0:
#         return response_data[response_index]['bot_response']
    
#     return random_responses.get_random_response()

# def main():
#     while True:
#         user_input: str = input('You: ')
#         print('Bot:', get_response(user_input))

# if __name__ == '__main__':
#     main()


# # # # # # # SECTION 20 TIPS & TRICKS # # # # # # # 

# # # # # # # F-Strings are powerful # # # # # # #

text: str = 'SAMPLE'
print(f'{text:20}: hello')
print(f'{text:<20}: hello')
print(f'{text:>20}: hello')
print(f'{text:^20}: hello')

print(f'{text:_<20}: hello')
print(f'{text:_>20}: hello')
print(f'{text:_^20}: hello')

number:float = 10_000.123456
print(f'{number:.2f}')
print(f'{number:,.2f}')

number2: int = 1_000_000
print(f'{number2:.0e}')

# # # # # # # Tuples & Type Hinting # # # # # # #

numbers: tuple[int | str, ...] = (12, 'hello', 1234)

# # # # # # # Flattening Lists # # # # # # #
from typing import Iterable

people: list = [['Mario', 'Luigi'], ['James', 'Bob']]
new_list: list[str] = []
for names in people:
    for name in names:
        new_list.append(name)

new_list2: list[str] = [name
                        for names in people
                        for name in names]


def flatten(iterable: Iterable) -> list:
    l: list = []
    for item in iterable:
        if isinstance(item, Iterable) and not isinstance(item, str):
            l.extend(flatten(item))
        else:
            l.append(item)
    return l

print(new_list)
print(new_list2)
print(flatten(people))

# # # # # # # Elipses # # # # # # #
print(...)

# # # # # # # Linting # # # # # # #
# pylint main.py in console

def do_something():
    print('Hello world')

class Fruit:
    def __init__(self):
        print('I am a fruit')
    
    def explode(self):
        pass

fruit: Fruit = Fruit()
do_something()


# # # # # # # #noqa # # # # # # #
import math, random # NOQA

math.sqrt(10)
random.random()