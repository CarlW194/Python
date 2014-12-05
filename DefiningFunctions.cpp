#Funtion definition is here
def changeme(myList):
	"This changes a passed list into this funtion"
	myList.append([1,2,3,4]);
	print "Values inside the funtion", myList
	return 

#Now you can call changeme function
myList=[10,20,30];
changeme(myList);
print "Values outside of function", myList
