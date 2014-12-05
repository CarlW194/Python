fo = open("foo.txt", "r+")
str = fo.read(10);
print "Read String is : ", str

#check position
position = fo.tell();
print "Current File position: ", position

#Reposition pointer at the beginning once again
position = fo.seek(0, 0);
str = fo.read(10);
print "Again read String is : ", str
fo.close()
