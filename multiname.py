# Import the sys package 
import sys

# Check for errors
# Doing this as a separate code to main code makes better design 
if len(sys.argv) < 2:
    # What happens if the user doesn't input their name
    sys.exit("too few arguments")
elif len(sys.argv) > 2: 
    # What happens if the user puts in more than one name 
    sys.exit("too many arguments")

# Print name tags
# If you run this in the terminal, can include name in the command line
print("Hello, my name is", sys.argv[1])
