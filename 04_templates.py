"""
4. String Template (od Pythonu 2)
"""

from string import Template

template = Template("My name is $name and I am $age")

string = template.substitute(name="Bob", age=33)
print(string)

# nefunkcni
# print(template.substitute(name="Bob"))
print(template.safe_substitute(name="Bob"))


"""
4. 1
Šablony lze nahradit řetězcem s parametry, které se později doplní.
"""
formated_string = "Your name is {name} and you are {age}"
name = input("Tell me your name: ")
age = input("How old are you?: ")
print(formated_string.format(name=name, age=age))


"""
Jaký ze způsobů kdy použít?
 
Pokud můžeme řetězec složit do finální podoby hned, použijeme F-String. 

V případě pozdějšího doplnění proměnných do řetězce použijeme String Template nebo strong.format()
Druhý jmenovný způsob použijeme před Template v případě, že potřebujeme mít větší kontrolu 
nad formátem proměnných. 

Ve všech ostatních případech preferujeme F-String. 
"""

