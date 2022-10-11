"""
5. Pokročilé formátování
https://peps.python.org/pep-3101/
"""

"""
5.1 Přístup k atributům objektu
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"I am {self.name}"


jose = Person("Jose", 44)
print("My name is {0.name} and I am {0.age}".format(jose))


"""
5.2 Přístup k položkám ve slovníku
"""
filomena = {"name": "Filomena", "age": 55}
print("My name is {0[name]} and I am {0[age]}".format(filomena))


"""
5.3 Výplň a odsazení
"""

print("{0:>+10}".format(15))
print("{0:<+10}".format(15))
print("{0:=+10}".format(15))
print("{0:#^10}".format(15))


"""
5.4 str a repr
"""
charlie = Person(name="Charlie", age=22)

print("{!r}".format(charlie))
print("{!s}".format(charlie))
print("{}".format(charlie))
