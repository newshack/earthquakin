
# make a function called greeting that asks for your name
# def command creates a function
def greeting():
	name = raw_input("what is your name? ")
	print "Hello world, " + name

def hello(name):
	print "Hello, " + name

def add(a, b):
	return a + b

hello("Alex")

print add(2, 3) + add(4, 5)