
import time
import random
import keyboard
import os


print()
print()
print(" ************************* Welcome to the first of end playing ************************* ")
print()
print()




"""
The structure inside which, all will be done
"""

def functionStructure():

	
	print()
	print()
	print("\t\t\t Don't forget that is just a play... \n")
	print("\t do -----> a        to the left")
	print("\t do -----> f        to the right")
	print("\t do -----> q        to quit \n")
	entry = input("Get your chance... ")
	print()
	print()
	
	aff = "!!!!!"
	test = ""
	score = 0
	variableToGetValueFromUser = 0	
	while(entry != "q"):
		variableToGetValueFromUser += 1
		rightValueA = random.choice([7, 15, 25, 33, 45, 55, 65])
		rightValueF = random.choice([41, 51, 61, 66, 14, 24, 33])
		for va in range(0, 8):
			for ve in range(0, 83):
				if(va == 0 or va == 7):  # the creation of the box that'll be served as the all structure...---------------
			
				# if the choice is about the right ----------------------------------------------------------------------------
					if(entry == "f"):
					
					
					
						if(va == 7 and (ve in range(40, 75))):
							print(" ", end="")
						elif(va == 7 and (ve in range(1, 6) or (ve in range(74, 80)))):
							print("*", end="")
						elif(va == 7 and(ve in range(6, 10))):
							print(" ", end="")
						elif(va == 7):
							print("^", end="")
						else:
							print("*", end="")
					# if the choice is about the left------------------------------------------------------------------
					elif(entry == "a"):
						# must underline, each value represents the moment column
						
					
						if(va == 7 and (ve in range(5, 40))):
							print(" ", end="")
						elif(va == 7 and (ve in range(1, 6) or (ve in range(74, 80)))):
							print("*", end="")
						elif(va == 7 and(ve in range(70, 74))):
							print(" ", end="")
						elif(va == 7):
							print("^", end="")
						else:
							print("*", end="")
				
					# At this part, no direction was selected ----------------------------------------------------------------
					else:
						print("*", end="")
				else: # now, what about happening inside of our structure-------------------------------------------------------------
					time.sleep(0.05)
				
				
					if(ve == 0 or ve == 79):
						print("*", end = "")
					elif((entry == "f") and ve == rightValueF):
						if(va == 6 and (rightValueF in range(10, 40))):
							print(" Good", end="")
							test = "good"
							score += 1
						if(va == 6 and (rightValueF in range(40, 80))):
							print(" Bad", end="")
							test = "bad"
						elif(va != 6):
							print(aff, end="")
							
					elif((entry == "a") and ve == rightValueA):
						if(va == 6 and (rightValueA in range(30, 70))):
							print(" Good", end="")
							test = "good"
							score += 1
						if(va == 6 and (rightValueA in range(5, 40))):
							print(" Bad", end="")
							test = "bad"
						elif(va != 6):
							print(aff, end="")
					else:
						if(ve in range(78, 80)):
							continue
						else:
							print(" ", end="")
			print("\n")
			
			
			
						
			
			print("\n")

		
		print("\t\t\t\t SCORE: " + str(score) )
		print()
		print(" Result of this run is " + test) 
		
		
		
		if(variableToGetValueFromUser == 3):
			print("\t\t\t\t\t\t\t\t\t Get other chance: ' a -> left,  f -> right,  q -> quit'     ") 
			enTest = input("...    ")
			if(enTest not in ["a", "f", "q"]):
				entry = entry
			else:
				entry = enTest
			variableToGetValueFromUser = 0
		else:
			entry = entry
		
		#os.system('clear')
		print()







functionStructure()










































