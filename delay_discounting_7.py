#delay discounting procedure to collect a single indifference point at 7 days delay and magnitude = $10
#immediate option can appear on the right or the left (randomized)
#trials are presented in a randomized order

#using shuffle from numpy.random but I have not removed the other modules which were being used in a psycopy
#program I have been studying to learn python
import numpy
import scipy

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle

#each question is presented in this format although some questions are reverse coded (immediate option on the right)
def survey_item(left_amount, left_delay, right_amount, right_delay, trial_number, trial_type):
		print "\n ****** \n ******" * 12
		print "Pick which one you would prefer \n"
		print "Remember there are no wrong answers"
		print "\n ****** \n ******" * 7
		print "\tWould you rather have $%s DOLLARS %s or have $%s DOLLARS %s" % (left_amount, left_delay, right_amount, right_delay)
		print "\t____________________LEFT OPTION (v)_________RIGHT OPTION(n)_____________\n"
		response = raw_input("\t >>>>>>>>> ")
		#more code comming soon to pass this to a file to store response and trial type)
		print response, trial_number, trial_type

def trial_1():
	arr_in = np.arange(2)
	np.random.shuffle(arr_in)
	am_SS = 5.00
	am_LL = 10
	del_SS = "TODAY"
	del_LL = "IN 7 DAYS"
	if arr_in[0] == 0: 
		survey_item(am_SS, del_SS, am_LL, del_LL, 1, 1)
	else:
		survey_item(am_LL, del_LL, am_SS, del_SS, 1, 2)

def trial_2():
	arr_in = np.arange(2)
	np.random.shuffle(arr_in)
	am_SS = 7.50
	am_LL = 10
	del_SS = "TODAY"
	del_LL = "IN 7 DAYS"
	if arr_in[0] == 0: 
		survey_item(am_SS, del_SS, am_LL, del_LL, 2, 1)
	else:
		survey_item(am_LL, del_LL, am_SS, del_SS, 2, 2)	    

def trial_3():
	arr_in = np.arange(2)
	np.random.shuffle(arr_in)
	am_SS = 8.75
	am_LL = 10
	del_SS = "TODAY"
	del_LL = "IN 7 DAYS"
	if arr_in[0] == 0: 
		survey_item(am_SS, del_SS, am_LL, del_LL, 3, 1)
	else:
		survey_item(am_LL, del_LL, am_SS, del_SS, 3, 2)	   

def trial_4():
	arr_in = np.arange(2)
	np.random.shuffle(arr_in)
	am_SS = 9.38
	am_LL = 10
	del_SS = "TODAY"
	del_LL = "IN 7 DAYS"
	if arr_in[0] ==0:
		survey_item(am_SS, del_SS, am_LL, del_LL, 4, 1)
	else:
		survey_item(am_LL, del_LL, am_SS, del_SS, 4, 2)		

arr = np.arange(4)
np.random.shuffle(arr)
print arr[0], arr[1], arr[2], arr[3]	

def runnit(enter):
	if enter == 0: 
		trial_1()
	else: 
		if enter == 1:
			trial_2()
		else: 
			if enter == 2:
				trial_3()
			else: 
				if enter == 3:
					trial_4()

runnit(arr[0])
runnit(arr[1])
runnit(arr[2])
runnit(arr[3])


#arr = trial_1(), trial_2(), trial_3(), trial_4()
#np.random.shuffle (arr)
