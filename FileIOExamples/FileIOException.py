try:
	fh=open("testFile", "w")
	fh.write("This is my test file for exception handling")
except IOErro:
	print "Error: cant find file or read data"
else:
	print "Written content in the file sucessfull"
	fh.close()
