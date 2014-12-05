total=0; #this is the global variable

# Function defintion is here
def sum(arg1, arg2):
	#Add both the parameters and return them.
	total = arg1 + arg2; # here total is local variable.
	print "Inside the function local total : ", total
	return total;

#Now you can call the function
sum(10,20);
print "Outside the function global total : ", total
