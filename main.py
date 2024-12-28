# If else
print('IF ELSE')
text = 'cd'

if text == 'Hello':
        print('Bot: Hello!')
elif text == 'Bye':
        print('Bot: Goodbye!')
else:
        print('I did not understand' )

print('Succes') if 3 > 2 else print('failure')
print()

# For loop
print('FOR LOOP')
people: list[str] =['Mario', 'Luigi', 'Peach', 'Toad'] 

for person in people:
        print(f'Hello, {person}')

for number in range(10):
        print(number)

print()

# While Loop
print('WHILE LOOP')

a = 0
while a < 10:
        print(a)
        a += 1