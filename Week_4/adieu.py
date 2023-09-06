# Import the inflect package
import inflect
p = inflect.engine()

# Create an empty list for the names
names = list()

while True:
    try:
        # If user inputs a name, adds it to the list
        name = input("Name: ")
        names.append(name)
    except EOFError:
        # If inputs control-d, breaks the loop
        break

# Prints the list of names, formatted with "... and, ..."
print("Adieu, adieu, to " + p.join(names))