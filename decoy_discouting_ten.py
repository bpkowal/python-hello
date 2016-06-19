from sys import exit
from random import randint

import numpy
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle

filler = "\n ********" * 25

Instructions = " %s \n Pick which one you would prefer \n Remember there are no wrong answers \n ****** \n ******" % filler

def Prompt(am_SS, am_LL, del_SS, del_LL):
		am_SS = round(am_SS,2)
		am_LL = round(am_LL,2)
		# sets decoy attributes
		if am_SS > am_LL:
			am_decoy = am_SS
			del_decoy = del_SS
		else:
			am_decoy = am_LL
			del_decoy = del_LL
		if del_decoy == "IN 1 DAY":
			del_decoy ="IN 2 DAYS"
		elif del_decoy =="IN 7 DAYS":
			del_decoy ="IN 14 DAYS"
		elif del_decoy =="IN 30 DAYS":
			del_decoy ="IN 60 DAYS"
		elif del_decoy =="IN 180 DAYS":
			del_decoy ="IN 360 DAYS"
		elif del_decoy =="IN 365 DAYS":
			del_decoy="IN 730 DAYS"
		elif del_decoy =="IN 1,825 DAYS":
			del_decoy= "IN 3,650 DAYS"
		else:
			del_decoy="18,250 DAYS"
		
		space_stuff_a = len(del_decoy)
		space_stuff_b = len(str(am_decoy))
		space_fix = ("_")*(23-space_stuff_a-space_stuff_b)
		space_stuff_c = len(del_SS)
		space_stuff_d = len(del_LL)
		space_fix_two = ("_")*(space_stuff_c - space_stuff_d)
        # determines random shadow decoy location left, middle, right
		arr_in = np.arange(3)
		np.random.shuffle(arr_in)
		
		if arr_in[0] == 0: 
			print "\tWould you rather have\n%s$ %s DOLLARS %s, %s $%s DOLLARS %s, %s or $%s DOLLARS %s" % (space_fix, am_SS, del_SS, space_fix, am_LL, del_LL, space_fix, am_decoy, del_decoy)
			print "_____%s LEFT OPTION (v) ___%s%s MIDDLE OPTION(n) ____%s%s NOT A CURRENT OPTION\n" % (space_fix, space_fix_two, space_fix, space_fix_two, space_fix)
		elif arr_in[0] == 1:
			print "\tWould you rather have\n%s $%s DOLLARS %s, %s $%s DOLLARS %s, %s or $%s DOLLARS %s" % (space_fix, am_decoy, del_decoy, space_fix, am_SS, del_SS, space_fix, am_LL, del_LL)
			print "__%s NOT A CURRENT OPTION_____%s%s MIDDLE OPTION(v)_____%s%s RIGHT OPTION(n)\n" % (space_fix, space_fix_two, space_fix, space_fix_two, space_fix)
		else:
			print "\tWould you rather have\n%s $%s DOLLARS %s, %s $%s DOLLARS %s, %s or $%s DOLLARS %s" % (space_fix, am_SS, del_SS, space_fix, am_decoy, del_decoy, space_fix, am_LL, del_LL)
			print "_____%s LEFT OPTION (v) __%s%s NOT A CURRENT OPTION_____%s%s RIGHT OPTION(n)\n" % (space_fix, space_fix_two, space_fix, space_fix_two, space_fix)
			

class Scene(object):

	def enter(self):	
		exit(1)
		
class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map
	
	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')
		
		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
			
		current_scene.enter()

class Trial_1(Scene):
		
	def enter(self):
		am_SS_adj = 5.0
		am_LL = 10.0
		del_SS = "TODAY"
		del_LL = "IN 1 DAY"
		
		i = 10
		lower = 5.0

		while i > 5 :
			arr_in = np.arange(2)
			np.random.shuffle(arr_in)
			if arr_in[0] == 0: 
				Prompt(am_SS_adj, am_LL, del_SS, del_LL)
				response = raw_input("\t >>>>>>>>> ")
				if response == "v": 
					am_SS_adj = am_SS_adj - (lower)/2 
					i = i -1
				elif response =="n":				
					am_SS_adj = am_SS_adj + (lower)/2
					i = i -1
				else:
					print "Please chose only v or n"
					lower = lower*2
			else:
				Prompt(am_LL, am_SS_adj, del_LL, del_SS)
				response = raw_input("\t >>>>>>>>> ")
				if response == "v":
					am_SS_adj = am_SS_adj + (lower)/2
					i = i -1
				elif response == "n":
					am_SS_adj = am_SS_adj - (lower)/2
					i = i -1
				else:
					print "Please chose only v or n"
					lower = lower*2
			
			lower = lower/2
			
		print round(am_SS_adj,2)
	
		return 'trial_2'
		
class Trial_2(Scene):
		
	def enter(self):
		am_SS_adj = 5.0
		am_LL = 10.0
		del_SS = "TODAY"
		del_LL = "IN 7 DAYS"
		
		i = 10
		lower = 5.0

		while i > 5 :
			arr_in = np.arange(2)
			np.random.shuffle(arr_in)
			if arr_in[0] == 0: 
				Prompt(am_SS_adj, am_LL, del_SS, del_LL)
				response = raw_input("\t >>>>>>>>> ")
				if response == "v": 
					am_SS_adj = am_SS_adj - (lower)/2 
					i = i -1
				elif response =="n":				
					am_SS_adj = am_SS_adj + (lower)/2
					i = i -1
				else:
					print "Please chose only v or n"
					lower = lower*2
			else:
				Prompt(am_LL, am_SS_adj, del_LL, del_SS)
				response = raw_input("\t >>>>>>>>> ")
				if response == "v":
					am_SS_adj = am_SS_adj + (lower)/2
					i = i -1
				elif response == "n":
					am_SS_adj = am_SS_adj - (lower)/2
					i = i -1
				else:
					print "Please chose only v or n"
					lower = lower*2
			
			lower = lower/2
			
		print round(am_SS_adj,2)
	
		return 'trial_3'

class Trial_3(Scene):
		
	def enter(self):
		am_SS_adj = 5.0
		am_LL = 10.0
		del_SS = "TODAY"
		del_LL = "IN 30 DAYS"
		
		i = 10
		lower = 5.0

		while i > 5 :
			arr_in = np.arange(2)
			np.random.shuffle(arr_in)
			if arr_in[0] == 0: 
				Prompt(am_SS_adj, am_LL, del_SS, del_LL)
				response = raw_input("\t >>>>>>>>> ")
				if response == "v": 
					am_SS_adj = am_SS_adj - (lower)/2 
					i = i -1
				elif response =="n":				
					am_SS_adj = am_SS_adj + (lower)/2
					i = i -1
				else:
					print "Please chose only v or n"
					lower = lower*2
			else:
				Prompt(am_LL, am_SS_adj, del_LL, del_SS)
				response = raw_input("\t >>>>>>>>> ")
				if response == "v":
					am_SS_adj = am_SS_adj + (lower)/2
					i = i -1
				elif response == "n":
					am_SS_adj = am_SS_adj - (lower)/2
					i = i -1
				else:
					print "Please chose only v or n"
					lower = lower*2
			
			lower = lower/2
			
		print round(am_SS_adj,2)
	
		return 'trial_4'

class Trial_4(Scene):
		
	def enter(self):
		am_SS_adj = 5.0
		am_LL = 10.0
		del_SS = "TODAY"
		del_LL = "IN 180 DAYS"
		
		i = 10
		lower = 5.0

		while i > 5 :
			arr_in = np.arange(2)
			np.random.shuffle(arr_in)
			if arr_in[0] == 0: 
				Prompt(am_SS_adj, am_LL, del_SS, del_LL)
				response = raw_input("\t >>>>>>>>> ")
				if response == "v": 
					am_SS_adj = am_SS_adj - (lower)/2 
					i = i -1
				elif response =="n":				
					am_SS_adj = am_SS_adj + (lower)/2
					i = i -1
				else:
					print "Please chose only v or n"
					lower = lower*2
			else:
				Prompt(am_LL, am_SS_adj, del_LL, del_SS)
				response = raw_input("\t >>>>>>>>> ")
				if response == "v":
					am_SS_adj = am_SS_adj + (lower)/2
					i = i -1
				elif response == "n":
					am_SS_adj = am_SS_adj - (lower)/2
					i = i -1
				else:
					print "Please chose only v or n"
					lower = lower*2
			
			lower = lower/2
			
		print round(am_SS_adj,2)
	
		return 'trial_5'

class Trial_5(Scene):
		
	def enter(self):
		am_SS_adj = 5.0
		am_LL = 10.0
		del_SS = "TODAY"
		del_LL = "IN 365 DAYS"
		
		i = 10
		lower = 5.0

		while i > 5 :
			arr_in = np.arange(2)
			np.random.shuffle(arr_in)
			if arr_in[0] == 0: 
				Prompt(am_SS_adj, am_LL, del_SS, del_LL)
				response = raw_input("\t >>>>>>>>> ")
				if response == "v": 
					am_SS_adj = am_SS_adj - (lower)/2 
					i = i -1
				elif response =="n":				
					am_SS_adj = am_SS_adj + (lower)/2
					i = i -1
				else:
					print "Please chose only v or n"
					lower = lower*2
			else:
				Prompt(am_LL, am_SS_adj, del_LL, del_SS)
				response = raw_input("\t >>>>>>>>> ")
				if response == "v":
					am_SS_adj = am_SS_adj + (lower)/2
					i = i -1
				elif response == "n":
					am_SS_adj = am_SS_adj - (lower)/2
					i = i -1
				else:
					print "Please chose only v or n"
					lower = lower*2
			
			lower = lower/2
			
		print round(am_SS_adj,2)
	
		return 'trial_6'

class Trial_6(Scene):
		
	def enter(self):
		am_SS_adj = 5.0
		am_LL = 10.0
		del_SS = "TODAY"
		del_LL = "IN 1,825 DAYS"
		
		i = 10
		lower = 5.0

		while i > 5 :
			arr_in = np.arange(2)
			np.random.shuffle(arr_in)
			if arr_in[0] == 0: 
				Prompt(am_SS_adj, am_LL, del_SS, del_LL)
				response = raw_input("\t >>>>>>>>> ")
				if response == "v": 
					am_SS_adj = am_SS_adj - (lower)/2 
					i = i -1
				elif response =="n":				
					am_SS_adj = am_SS_adj + (lower)/2
					i = i -1
				else:
					print "Please chose only v or n"
					lower = lower*2
			else:
				Prompt(am_LL, am_SS_adj, del_LL, del_SS)
				response = raw_input("\t >>>>>>>>> ")
				if response == "v":
					am_SS_adj = am_SS_adj + (lower)/2
					i = i -1
				elif response == "n":
					am_SS_adj = am_SS_adj - (lower)/2
					i = i -1
				else:
					print "Please chose only v or n"
					lower = lower*2
			
			lower = lower/2
			
		print round(am_SS_adj,2)
	
		return 'trial_7'

class Trial_7(Scene):
		
	def enter(self):
		am_SS_adj = 5.0
		am_LL = 10.0
		del_SS = "TODAY"
		del_LL = "IN 9,125 DAYS"
		
		i = 10
		lower = 5.0

		while i > 5 :
			arr_in = np.arange(2)
			np.random.shuffle(arr_in)
			if arr_in[0] == 0: 
				Prompt(am_SS_adj, am_LL, del_SS, del_LL)
				response = raw_input("\t >>>>>>>>> ")
				if response == "v": 
					am_SS_adj = am_SS_adj - (lower)/2 
					i = i -1
				elif response =="n":				
					am_SS_adj = am_SS_adj + (lower)/2
					i = i -1
				else:
					print "Please chose only v or n"
					lower = lower*2
			else:
				Prompt(am_LL, am_SS_adj, del_LL, del_SS)
				response = raw_input("\t >>>>>>>>> ")
				if response == "v":
					am_SS_adj = am_SS_adj + (lower)/2
					i = i -1
				elif response == "n":
					am_SS_adj = am_SS_adj - (lower)/2
					i = i -1
				else:
					print "Please chose only v or n"
					lower = lower*2
			
			lower = lower/2
			
		print round(am_SS_adj,2)
	
		return 'finished'

class Questions(Scene):

	def enter(self):
		print Instructions
		return 'trial_1'



class Finished(Scene):

	def enter(self):
		print filler
		print """ Thank you for your participation! \n Let your lab assistant know you are done now. \n ****** \n ******"""

class Map(object):
	
	trials = {
	'questions': Questions(),
	'trial_1': Trial_1(),
	'trial_2': Trial_2(),
	'trial_3': Trial_3(),
	'trial_4': Trial_4(),
	'trial_5': Trial_5(),
	'trial_6': Trial_6(),
	'trial_7': Trial_7(),
	'finished': Finished()
	}
	
	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def next_scene(self, scene_name):
		val = Map.trials.get(scene_name)
		return val
	
	def opening_scene(self):
		return self.next_scene(self.start_scene)



a_map = Map('questions')
a_game = Engine(a_map)
a_game.play()