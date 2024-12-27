# Basic Operators
print(2+2)
print(2*2)
print(2-2)
print(10/3)
print(10//3)
print(10%3)
print(10 ** 3)

print(10==10)
print(10!=10)
print(10==5)
print(10!=5)

a = 20
b = 40

print( a<b and 4>6 )
print( a<b or 5>6 )

numbers = [1,2,3,4]
print(1 in numbers)

# Strings
var = "text"
print(f"1 {var} 2")

# List
people: list[str] = ['Mario', 'Luigi', 'Peach', 'Toad']
pokemon: list[str] = ['Pikacu', 'Celebi']
people[0] = 'Chill Guy'
people.insert(2,'!!!')
people.append('To the end')
people.remove('Peach')
people.pop(0)
people.sort()
people.clear()
people.extend(pokemon)
print(people)

# Tuples
print('TUPLES')
tple: tuple = ('Mario' , 'Luigi', 'Peach')
tple_list: list[str] = list[tple]
tple_tuple : tuple = tuple[tple_list]
print(tple)
print()

# Sets
print('SETS')

items: set = {'Apple', 'Banana', 10, True}
items2: set = {'kiwi', 40, 'Banana', 'Apple'}
items.add('orange')
items.update(['carrot', 15])
items.remove('Apple')
items.discard('Banana')

new_set = items.union(items2)
new_set = items | items2
items |= items2
items.intersection_update(items2)
print(items)
print()

# Dictionaries
print('DICTIONARIES')
users = {'User1': 'Mario123', 
        'User2': 'Luigi456',
        'fruits':{'apple':10,
                'banana': 20}}

user1 = users['User1']
print(user1)
x = list(users.keys())
print(x)
y = list(users.values())
print(y)
users['User1'] = 'Toad789'
all = users.items()
print(all)

users.update({'hello': 123})
users.pop('hello')
print(users)
print(users['fruits'])
print(users['fruits']['apple'])