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

print()

# Break & continue
print('BREAK & CONTINUE')

for i in range(10):
        print(i)
        if i == 5:
                break

i = 0
while i<3:
        print(i)
        if i== 1:
                break

        i += 1

for i in range(5):
        if i == 3:
                continue

        print(i)

print()

# Pass 
print('PASS')

x , y = 10, 20
if x > y:
        pass

print()

# Loop Else
print('LOOP ELSE')

for i in range(5):
        print(i, end=' ')

        if i == 2:
                break
else:
        print('Succes')

print()

t = 0
while t < 3:
        print(t, end=' ')
        t+=1

        if t == 2:
                break
else:
        print('Succes')