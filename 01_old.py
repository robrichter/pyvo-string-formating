"""
1. starý způsob pomocí operátoru % (od Pythonu 2)
"""

"""
1.1 s jedním operandem 
"""
string_s = "Welcome to Pyvo number %s!" % 12.0
print(string_s)

print("Welcome to Pyvo number %d!" % 12.0)
print("Welcome to Pyvo number %d!" % int("12"))
print("Welcome to Pyvo number %f!" % 12)
print("Welcome to Pyvo number %x!" % 12)


"""
1.1 s více operandy 
"""

# nefunkcni
# string = "My name is %s and I am %d" % "Bob", "18"
# string = "My name is %s and I am %d" % ["Bob", "18"]

# funkcni
string = "My name is %s and I am %d" % ("Bob", 18)
print(string)
