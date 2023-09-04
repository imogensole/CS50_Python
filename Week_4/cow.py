import cowsay
import sys

# Check for errors 
if len(sys.argv) == 2: 
    cowsay.cow("hello, " + sys.argv[1])