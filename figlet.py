# Converts user text input into Frank, Ian and Glen's letters

# Import required packages
import sys
from pyfiglet import Figlet
import pyfiglet
import random

# define figlet and list of fonts
figlet = Figlet()
fonts = figlet.getFonts()

# Checks for errors
if len(sys.argv) == 3 and sys.argv[1] in ['-f', '--font']:
    f = sys.argv[2]
# checks if first command argument correct
elif sys.argv[1] not in ['-f', '--font']:
    # if not, raises error
    sys.exit("Invalid usage")
# if user doesn't input font, chooses at random
else:
    f = random.choice(fonts)

# Tries to find font input in list
try:
    figlet.setFont(font=f)
# if not found, raises error
except pyfiglet.FontNotFound:
    sys.exit("Invalid usage")

# asks for input phrase
phrase = input("Input: ")

# outputs using figlet
print(figlet.renderText(phrase))