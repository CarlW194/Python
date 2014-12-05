import time;

tick=time.time()
print "Number of ticks since 12:00am, January 1, 1970", tick

localTime=time.localtime(time.time())
print "Local current Time: ", localTime

normalTime=time.asctime(time.localtime(time.time()))
print "Local current normal time: ", normalTime
