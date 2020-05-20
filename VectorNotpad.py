import tkinter 
import os	 
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import random
#imported python funtion ;)

import anki_vector
from math import cos
from anki_vector import lights
import time
from anki_vector.util import degrees, distance_mm, speed_mmps
from PIL import Image


# Connection to vector function



def saytext( x ):
	with anki_vector.Robot() as robot:
				

				
				robot.behavior.set_head_angle(degrees(45))
				if (x == 0):
					robot.behavior.say_text("Opening vector Note Pad for you now boss  !")
					
					time.sleep(1)
				if (x == 1):
					robot.behavior.set_head_angle(degrees(45))
					robot.behavior.say_text("Closeing vector Note Pad  with explosives")
					animation = 'anim_holiday_hny_fireworks_01'
					robot.anim.play_animation('anim_holiday_hny_fireworks_01')
					time.sleep(0)
				if (x == 2):
					robot.behavior.set_head_angle(degrees(45))
					robot.behavior.say_text("VectorNotepad is a totaly grovey text editor ,Starring ! Me ! and my cube! ")
					while not robot.world.connected_light_cube:
						robot.behavior.say_text("Cube can  be  bit shy some times")
						robot.world.connect_cube()
						robot.behavior.say_text("do it for me cube..")
					
						cube = robot.world.connected_light_cube
					
						colors = [ lights.red_light,
						lights.yellow_light,
						lights.green_light,
						lights.cyan_light,
						lights.blue_light,
						lights.magenta_light ]

						for j in range(2):
							for color in colors:
								cube.set_lights(color)
								time.sleep(0.4)
						
								cube.set_lights_off()
								time.sleep(1)
				if (x == 3):
					robot.behavior.set_head_angle(degrees(45))
					robot.behavior.say_text("Mr Cube's opeing the files boss!")
					time.sleep(0.1)
				if (x == 4):
					robot.behavior.set_head_angle(degrees(45))
					robot.behavior.say_text("New file made well Done Mr Cube!")
					time.sleep(0.5)
				if (x == 5):
					robot.behavior.set_head_angle(degrees(45))
					robot.behavior.say_text("ok Mr Cube save this for later!")
					time.sleep(1)
				if (x == 6):
					robot.behavior.set_head_angle(degrees(45))
					robot.behavior.say_text("O! John he is so be on Help! !")
					time.sleep(1)
				if (x == 7):
					robot.behavior.set_head_angle(degrees(45))
					robot.behavior.say_text(" Mr cube!  is cutting it!")
					time.sleep(1)
				if (x == 8):
					robot.behavior.set_head_angle(degrees(45))
					robot.behavior.say_text("Mr Cube made a copy!")	
					time.sleep(1)
				if (x == 9):
					robot.behavior.set_head_angle(degrees(45))
					robot.behavior.say_text("Paste it Mr Cube !")
					time.sleep(1)

				else:
						robot.behavior.set_head_angle(degrees(00))
class VectorNotepad: 


	saytext( 0 )

	__root = Tk() 

	# default window width and height 
	__thisWidth = 300
	__thisHeight = 300
	__thisTextArea = Text(__root) 
	__thisMenuBar = Menu(__root) 
	__thisFileMenu = Menu(__thisMenuBar, tearoff=0) 
	__thisEditMenu = Menu(__thisMenuBar, tearoff=0) 
	__thisHelpMenu = Menu(__thisMenuBar, tearoff=0) 

	
	# To add scrollbar 
	__thisScrollBar = Scrollbar(__thisTextArea)	 
	__file = None

	def __init__(self,**kwargs): 

		# Set icon 
		try: 
				self.__root.wm_iconbitmap("Notepad.ico") 
		except: 
				pass

		# Set window size (the default is 300x300) 

		try: 
			self.__thisWidth = kwargs['width'] 
		except KeyError: 
			pass

		try: 
			self.__thisHeight = kwargs['height'] 
		except KeyError: 
			pass

		# Set the window text 
		self.__root.title("Untitled - VectorNotepad") 

		# Center the window 
		screenWidth = self.__root.winfo_screenwidth() 
		screenHeight = self.__root.winfo_screenheight() 
	
		# For left-alling 
		left = (screenWidth / 2) - (self.__thisWidth / 2) 
		
		# For right-allign 
		top = (screenHeight / 2) - (self.__thisHeight /2) 
		
		# For top and bottom 
		self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, 
											self.__thisHeight, 
											left, top)) 

		# To make the textarea auto resizable 
		self.__root.grid_rowconfigure(0, weight=1) 
		self.__root.grid_columnconfigure(0, weight=1) 

		# Add controls (widget) 
		self.__thisTextArea.grid(sticky = N + E + S + W) 
		
		# To open new file 
		self.__thisFileMenu.add_command(label="New", 
										command=self.__newFile)	 
		
		# To open a already existing file 
		self.__thisFileMenu.add_command(label="Open", 
										command=self.__openFile) 
		
		# To save current file 
		self.__thisFileMenu.add_command(label="Save", 
										command=self.__saveFile)	 

		# To create a line in the dialog		 
		self.__thisFileMenu.add_separator()										 
		self.__thisFileMenu.add_command(label="Exit", 
										command=self.__quitApplication) 
		self.__thisMenuBar.add_cascade(label="File", 
									menu=self.__thisFileMenu)	 
		
					
		# To give a feature of cut 
		self.__thisEditMenu.add_command(label="Cut", 
										command=self.__cut)			 
	
		# to give a feature of copy	 
		self.__thisEditMenu.add_command(label="Copy", 
										command=self.__copy)		 
		
		# To give a feature of paste 
		self.__thisEditMenu.add_command(label="Paste", 
										command=self.__paste)		 
		
		# To give a feature of editing 
		self.__thisMenuBar.add_cascade(label="Edit", 
									menu=self.__thisEditMenu)	 
 
		
		# To create a feature of description of the notepad 
		self.__thisHelpMenu.add_command(label="About VectorNotepad", 
										command=self.__showAbout) 
		self.__thisMenuBar.add_cascade(label="Help", 
									menu=self.__thisHelpMenu) 

		self.__root.config(menu=self.__thisMenuBar) 

		self.__thisScrollBar.pack(side=RIGHT,fill=Y)					 
		
		# Scrollbar will adjust automatically according to the content		 
		self.__thisScrollBar.config(command=self.__thisTextArea.yview)	 
		self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set) 
	
		
	def __quitApplication(self):
		saytext( 1 )
		self.__root.destroy() 
		# exit() 

	def __showAbout(self):
		saytext( 6 )
		showinfo("VectorNotepad Staring Vector","by Shodan1967 aka John Feeley") 
		saytext( 2 )
	def __openFile(self): 
		saytext( 3 )
		self.__file = askopenfilename(defaultextension=".txt", 
									filetypes=[("All Files","*.*"), 
										("Text Documents","*.txt")]) 

		if self.__file == "": 
			
			# no file to open 
			self.__file = None
		else: 
			
			# Try to open the file 
			# set the window title 
			self.__root.title(os.path.basename(self.__file) + " - VectorNotepad") 
			self.__thisTextArea.delete(1.0,END) 

			file = open(self.__file,"r") 

			self.__thisTextArea.insert(1.0,file.read()) 

			file.close() 

		
	def __newFile(self):
		
		self.__root.title("Untitled - VectorNotepad") 
		self.__file = None
		self.__thisTextArea.delete(1.0,END)
		saytext( 4 )

	def __saveFile(self): 
		saytext( 5 )
		if self.__file == None: 
			# Save as new file 
			self.__file = asksaveasfilename(initialfile='Untitled.txt', 
											defaultextension=".txt", 
											filetypes=[("All Files","*.*"), 
												("Text Documents","*.txt")]) 

			if self.__file == "": 
				self.__file = None
			else: 
				
				# Try to save the file 
				file = open(self.__file,"w") 
				file.write(self.__thisTextArea.get(1.0,END)) 
				file.close() 
				
				# Change the window title 
				self.__root.title(os.path.basename(self.__file) + " - Notepad") 
				
			
		else: 
			file = open(self.__file,"w") 
			file.write(self.__thisTextArea.get(1.0,END)) 
			file.close() 

	def __cut(self):
		saytext( 7 )
		self.__thisTextArea.event_generate("<<Cut>>") 

	def __copy(self): 
		self.__thisTextArea.event_generate("<<Copy>>") 
		saytext( 8 )
	def __paste(self): 
		self.__thisTextArea.event_generate("<<Paste>>") 
		saytext( 9 )
	def run(self): 

		# Run main application 
		self.__root.mainloop() 




# Run main application 
notepad = VectorNotepad(width=600,height=400) 
notepad.run()
