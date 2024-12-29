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