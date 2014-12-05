#loops


#while loop
count = 0
while (count < 9 ):
	print "Value of count :", count
	count+= count + 1

#for loop with letters
for letter in 'Python':
	print 'Current Letter: ', letter

#for loop with ints,nested loops
for num in range(10,20):  		#to iterate between 10 to 20
   	for i in range(2,num): 		#to iterate on the factors of the number
      		if num%i == 0:      	#to determine the first factor
         		j=num/i         #to calculate the second factor
         		print '%d equals %d * %d' % (num,i,j)
         		break 	#to move to the next number, the #first FOR
   		else:                  # else part of the loop
      			print num, 'is a prime number'


#continue  loop example
for letter in 'Python':     # First Example
   	if letter == 'h':
		continue
   	print 'Current Letter :', letter

var = 10                    # Second Example
while var > 0:              
   	var = var -1
   	if var == 5:
      		continue
   	print 'Current variable value :', var
print "Good bye!"


#Pass block loop example
for letter in 'Python': 
   	if letter == 'h':
      		pass
      		print 'This is pass block'
   	print 'Current Letter :', letter
print "Good bye!"
