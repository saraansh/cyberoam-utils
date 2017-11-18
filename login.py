#!/usr/bin/env python

from cyberoam import *

# Check login status after this interval.
STATUS_INTERVAL = 60 * 2

import sys

usr = sys.argv[1]
pwd = sys.argv[2]

if sendLoginRequest(usr,pwd):
    print 'Logged in with %s' %usr
    
    while True:
        sleep(STATUS_INTERVAL)

        if not checkLiveStatus(usr):
            print 'Logged Out!'
            break
else:
    print 'Error logging in!'
