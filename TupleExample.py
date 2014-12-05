#tuples cannot be updated 

tuple = ('abcd', 786, 2.23, 'john', 70.2)
tinyTuple = (123, 'john')

print tuple		#prints out full tuple
print tuple[0]		#prints tuple at position 0
print tuple[1:3]	#prints tuple starting at 2nd to 3rd
print tuple[2:]		#print starting from 3rd element onwards
print tinyTuple*2	#prints tinyTuple twice
print tuple + tinyTuple	#prints concatenated tuples	
