from sys import argv

script, first, second, third = argv

print "The script is called:", script

name = raw_input("What is your name? ")

print "%s, your first variable is:" % name, first
print "%s, your second variable is:" % name, second
print "%s, your third variable is:" % name, third

