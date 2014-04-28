################################################################################
# File Name:	Menus.py
# Author:		Debbie Heisler
# Date:			April 4, 2014
# Description:
#	This file contains all the menus needed for the contact manager. 
#	Each function will print out a menu.
################################################################################
""" Functions to print the various menus to a screen """

def printMainMenu():
	print()
	print("1. Print to screen")
	print("2. Search")
	print("3. Add contact")
	print("4. Delete contact")
	print("5. Write to file")
	print("6. Quit")
	print()
	
def printSearchMenu():
	print()
	print("0. First Name")
	print("1. Last Name")
	print("2. Email")
	print()
	
def printSearchCriteria(field):
	print()
	print("What string in the field " + field + " do you want to seach for?")
	
def printInvalidOption(command):
	print()
	print("", command , " is not a valid option.  Please select again.")

