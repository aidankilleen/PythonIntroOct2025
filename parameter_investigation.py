# parameter_investigation.py

# you can provide default values for parameters - times=1 is a sensible default

def greet (name, greeting="Welcome", times=1):

    for i in range(times):
        print (f"{greeting} {name}")


greet("Aidan", "Welcome", 3)
greet("Alice", "Welcome")
greet("Bob")
greet("Hans", "Wilkommen")
greet("Pierre", "Bienvenu")

# named parameters
# you can supply parameters with names
# you can put named parameters in any order
greet(times=4, name="Carol", greeting="Failte")
greet(name="Fred")

#print uses a combination of positional and named parameters
print(1, 2, 3, 4, 5, sep="-", end="\n\n")




