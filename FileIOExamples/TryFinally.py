try:
	fh = open("textFile", "w")
	fh.write("This is my test file for the exception handling!!")
finally:
	print "Error: can\'t find file or read date"
