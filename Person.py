################################################################################
# File name:	Person.py
# Author:	Debbie Heisler
# Date:		April 4, 2014
# Description:
#	This class represents a person.  It contains their first name,
#	last name, and email address.  It can print out itself
################################################################################
""" Person class contains methods and members to describe one person """

class Person:

    def __init__(self, fn, ln, em):
        """ Initialize a person with the give first name,
        last name, and email address
        """
        self.firstName = fn
        self.lastName = ln
        self.email = em

    def printToScreen(self):
        """ Prints the person information to the screen """
        formatted = '\t' + self.firstName + '\t\t' + self.lastName + \
            '\t\t' + self.email
        print(formatted)

    def printToFile(self, fn):
        """ Prints the person information to the given file, fn """
        formatted = self.firstName + "," + self.lastName + "," + self.email + "\n"
        fn.write(formatted)

    def inFirstName(self, match):
    	""" Returns true if match is contained in the first name.
    	False otherwise.  Case insensitive """
    	if (self.firstName.lower().find(match.lower()) < 0): 
    		return False
    	else: 
    		return True
    	
    def inLastName(self, match):
    	""" Returns true if match is contained in the last name.
    	False otherwise. Case insensitive """
    	if (self.lastName.lower().find(match.lower()) < 0):
    		return False
    	else:
    		return True
    	
    def inEmail(self, match):
    	""" Returns true if match is contained in the email address.
    	False otherwise.  Case insensitive """
    	if (self.email.lower().find(match.lower()) < 0):
    		return False
    	else:
    		return True
