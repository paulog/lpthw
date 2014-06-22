# Initialize variables
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# Demonstrate formatting strings 
print x
print y

# Demonstrate strings within strings within strings
print "I said: %r." % x
print "I also said: '%s'." % y

# Demonstrate %r with a boolean
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

# Demonstrate string concatenation
w = "This is the left side of..."
e = "a string with a right side."

print w + e
