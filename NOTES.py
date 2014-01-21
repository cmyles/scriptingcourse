"""
Formatting
"""

# Constant: all uppercase
ACCESSKEY = "123456"

# Object: first letter uppercase
Graph = newGraph(something)

# Variables: lowercase
graph = newGraph(somethingelse)

# Two or more words together

	# Option 1: use underscores
	old_list = ["hello","good","chap"]

	#Option 2: "camel case"
	oldList: = ["good day","sir"]

# Append variable type - e.g. to remember that an object is a list
# Some people add "List" at end, others start the name with "l", etc.
userNames = ["Bernie","John","Helen"]

userNamesList

lUserNames = ["Bernie","Helen"]									# this is a list
dUserNames = {"Bernie":"Research Fellow","Helen":"Director"}	# this is a dictionary
tUserNames = ("Bernie","Helen")									# this is a tuple, it's a read-only list

# System variable names: use double underscores
# system variables are hidden

__author__
__version__



"""
Python is a strongly-cast language; Java is not
"""

#Java:
string x = "hello world"	#Need to tell it in advance what type of variable it is

#Python:
x = "hello world"			#Can be any type of variable, it's defined once you give it a value
							# ==> useful to specify what type of object it is in the object name, as above



"""
Random notes
"""

# System word for missing is "None":

thingyList = ["1","2",None,"3"]


# To figure out everything you can do with an object, use dir in the terminal

dir("Hello!")	#will tell you everything you can do with the string "Hello"

for i in dir("Hello!"): print i 	# prints it nicely

# To use help:

help(thing)					# opens the help file for thing
help("something".upper)		# opens the help file for "something".upper
	
	# To get out of help, type Q