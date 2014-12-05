#define a function here.
def temp_convert(var):
	try:
		return int(var)
	except ValueError, Arguement:
		print "The arguement does not contain numbers\n", Arguement

#call above function
temp_convert("xyz");
