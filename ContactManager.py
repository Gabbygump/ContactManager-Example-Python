################################################################################
# File Name:	ContactManager.py
# Author:		Debbie Heisler
# Date:			April 4, 2014
# Description:
#	This is the contact manager main driver function/file. 
###############################################################################
""" Contact Manager main driver functions/files """

from Person import Person
from List import List
import Menus

quit = False		# global variable to make getting out of here easier
contactList = List()

def readInContacts():
	""" Read in the default contact list file """
	file = open('contacts.txt', 'r')
	for line in file:
		fields = line.split(',')
		peep = Person(fields[0].strip(), fields[1].strip(), fields[2].strip())
		contactList.addPerson(peep)
		
def printContactsToFile():
	""" Print the contacts to a file.  Will loop until get a good file name """
	while True:
		print("File Name")
		fn = raw_input()
		try:
			file = open(fn, 'w')
			contactList.printToFile(file)
			print("Contacts written to " + fn)
			break
		except IOError:
			continue

def addNewContact():
	""" Adds a new contact to the contact manager. Does no error checking """
	global contactList
	print("First Name:",)
	fn = raw_input()
	print("Last Name:",)
	ln = raw_input()
	print("Email:",)
	email = raw_input()
	peep = Person(fn, ln, email)
	contactList.addPerson(peep)

	
def handleFoundPerson(person, option):
	""" Error checks person.  Prints it or an error """
	if person is None:
		print("No one matches that criteria")
	elif option == "search":
		person.printToScreen()
	elif option == "delete":
		contactList.deletePerson(person)

def checkSearchInput(selected, option):
	""" Handles the input for searching. """
	if selected == 0:
		Menus.printSearchCriteria("First Name")
		searchStr = raw_input()
		peep = contactList.matchPersonByFirstName(searchStr)
		handleFoundPerson(peep, option)
	elif selected == 1:
		Menus.printSearchCriteria("Last Name")
		searchStr = raw_input()
		peep = contactList.matchPersonByLastName(searchStr)
		handleFoundPerson(peep, option)
	elif selected == 2:
		Menus.printSearchCriteria("Email")
		searchStr = raw_input()
		peep = contactList.matchPersonByEmail(searchStr)
		handleFoundPerson(peep, option)
	else:
		print("That is not a valid selection")


def searchForPerson(option):
	""" Handles the option to search for a person to print or delete """
	Menus.printSearchMenu()
	while True:
		try:
			selection = int(raw_input())
			checkSearchInput(selection, option)
			break
		except ValueError:
			print("Numbers only.  Try again")
			continue

def checkInput(selected):
	""" Checks the input to make sure it is a valid main menu option """
	global quit
	if selected == 1:
		contactList.printToScreen()
	elif selected == 2:
		searchForPerson("search")
	elif selected == 3:
		addNewContact()
	elif selected == 4:
		searchForPerson("delete")
	elif selected == 5:
		printContactsToFile()
	elif selected == 6:
		quit = True
	else:
		Menus.printInvalidOption(selected)
		

#####################
# The Main function
####################

readInContacts()

while (quit == False):
	Menus.printMainMenu()
	try:
		selection = int(raw_input())
		checkInput(selection)
	except ValueError:
		continue
