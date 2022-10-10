"""
2. String metoda format() - od Pythonu 3.0
"""
string = "My name is {} and I am {}".format("Bob", 18)
print(string)

string = "My name is {} and I am {}"
print(string.format("Natas", "666"))

print("My name is {1} and I am {0}".format("Natas", "666"))

from math import pi
print("My name is {} and I am {:.3f}".format("Pi", pi))

string = "My name is {name}, I am {age:d} and {height:.2f} feet tall".format(
    name="John",
    age=33,
    height=4.3333
)

print(string)
