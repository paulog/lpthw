# Import modules
from sys import argv

script, filename = argv

# Open the file from the command line argument
txt = open(filename)

# Print out the contents of the file
print "Here's your file %r:" % filename
print txt.read()

txt.close()

# As for a new file to read
print "Type the filename again:"
file_again = raw_input("> ")

# Print out the contents of the raw_inputted file
txt_again = open(file_again)

print txt_again.read()

txt_again.close()
