# Current time
import time;
localtime=time.localtime(time.time())
print("current time",localtime)
formattime=time.asctime(time.localtime())
print("formatted time",formattime)