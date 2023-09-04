# Import the sys package 
import sys

# Check for errors
# Doing this as a separate code to main code makes better design 
if len(sys.argv) < 2:
    # What happens if the user doesn't input their name
    sys.exit("too few arguments")

# Print name tags
# If you run this in the terminal, can include name in the command line
# iterates over each argument in the input list 
# Uses a slice to exclude the first item (the filename)
for arg in sys.argv[1:]:
    # prints each nametag 
    print("Hello, my name is", arg)