"""
3. F Stringy - od Pythonu 3.6
"""
from random import randint

string = f"My name is {'Bob'} and I am {33}"
print(string)

print(f'My name is {"Bob"} and I am {33}')
print(f'''My name is {"Bob"} and I am {33}''')
print(f"""My name is {"Bob"} and I am {33}""")

print(f'My name is {{Bob}} and I am {33}')

# nefunkcni
# print(f"My name is {"Bob"} and I am {33}")
# print(f'My name is {'Bob'} and I am {33}')


print("\n\nPoužití výrazu jako parametru")
def get_random_age():
    return randint(1, 100)

print('My name is %s and I am %s' % ("Poo", get_random_age()))
print('My name is {} and I am {}'.format("Poo", get_random_age()))
print(f'My name is {"Poo"} and I am {get_random_age()}')


'''
F Stringy - operátor =, od Pythonu 3.8
'''
age = 44
height = 180
weight = 80
print(f"age={age} height={height} weight={weight}")
print(f"{age=} {height=} {weight=}")

