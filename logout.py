#!/usr/bin/env python

from cyberoam import *

import sys

cmd = sys.argv[1]
sendLogoutRequest(cmd)
