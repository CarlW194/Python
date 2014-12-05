try:
	fh = open("testFile", "w")
	try:
		fh.write("This is my test file for exception handling!!")
	finally:
		print "going to close the file"
		fh.close()
except IOError:
	print "Error: can\'t find file or read data"
