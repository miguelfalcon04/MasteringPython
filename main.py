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

with open('sample.text', 'r') as text:
    t : list[str] = text.readlines()
    print(text.readline())
    print(text.read())
    print(t)


# # WRITING & CREATING FILES
with open('sample.text', 'a+') as text:
    text.write('\n1234')
    text.seek(0)
    print(text.read())

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