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
		print "\tWould you rather have $%s DOLLARS %s or have $%s DOLLARS %s" % (am_SS, del_SS, am_LL, del_LL)
		print "\t____________________LEFT OPTION (v)_________RIGHT OPTION(n)_____________\n"


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
		del_LL = "IN ONE DAY"
		
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
		del_LL = "IN ONE WEEK"
		
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
		del_LL = "IN ONE MONTH"
		
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
		del_LL = "IN SIX MONTHS"
		
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
		del_LL = "IN ONE YEAR"
		
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
		del_LL = "IN FIVE YEARS"
		
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
		del_LL = "IN 25 YEARS"
		
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