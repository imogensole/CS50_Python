# prompts user for an input string and automatically coverts any codes/aliases into emojis

# import the emoji package 
import emoji 

# prompt user for input 
phrase = input("Input: ")

# convert codes to corresponding emoji 
print(emoji.emojize(phrase))
