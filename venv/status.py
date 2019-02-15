#!/usr/bin/python
# status.py - runs command line utility based on input
import sys
import os
import psutil
import time
# Get the total number of args passed to the demo.py
total = len(sys.argv)

def seconds_elapsed():
    return time.time() - psutil.boot_time()


# Get the arguments list
cmdargs = str(sys.argv)

cmdid = str(sys.argv[1])
if cmdid == '1':
    msg = os.popen('ver ' + cmdid).read()
elif cmdid == '2':
    msg = seconds_elapsed()
else:
    msg = "Not Implemented"

print msg
