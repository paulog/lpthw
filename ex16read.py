# Import modules
from sys import argv

script, filename = argv

# Open the file from the command line argument
txt = open(filename)

# Print out the contents of the file
print txt.read()

txt.close()
