"""
3. F Stringy - od Pythonu 3.6
"""
from random import randint

name, age = ('Bob', 33)
string = f"My name is {name} and I am {age}"
print(string)

print(f'My name is {name} and I am {age}')
print(f'''My name is {name} and I am {age}''')
print(f"""My name is {name} and I am {age}""")

print(f'My name is {{name}} and I am {age}')

# nefunkcni
# print(f"My name is {"Bob"} and I am {33}")
# print(f'My name is {'Bob'} and I am {33}')

"""
3.1 Použití výrazu jako parametru - lze použít nejen v fstrings, i v předešlých způsobech
"""
print("\n\nPoužití výrazu jako parametru")


def get_random_age():
    return randint(1, 100)


print('My name is %s and I am %s' % ("Poo", get_random_age()))
print('My name is {} and I am {}'.format("Poo", get_random_age()))
print(f'My name is {"Poo"} and I am {get_random_age()}')


'''
3.2 F Stringy - operátor =, od Pythonu 3.8
'''
print("\n\nPouziti operator = pro doplneni nazvu promennych")

age = 44
height = 180
weight = 80
print(f"age={age} height={height} weight={weight}")  # zde si jmena promennych vypisu rucne
print(f"{age=} {height=} {weight=}")  # operator = za me jmena promennych doplni automaticky

