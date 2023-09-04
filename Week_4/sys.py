# Import the sys package 
import sys

try:
    # If you run this in the terminal, can include name in the command line
    print("Hello, my name is", sys.argv[1])
# What happens if there is no input in the command line...
except IndexError: 
    print("You need to input your name")