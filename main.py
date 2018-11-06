import time
import math
import os
import datetime

import importsExplanation

#Make sure to know how to define global functions an dhow to use them

def commenting_Explanation():
	print("# Is used for a single line comment")
	print("'''")
	print("These 3 quotes will comment for multiple lines")
	print("''' \n")
	print("Both the SingleLine comment and MultiLine comment WILL NOT WORK if it's inside a string")

def imports_Explanation():
	print("The more commonly used imports/libraries for more information:\n") 
	
	importDictionary = {
  		"Math": "Used for Simple Math operations",
  		"Time": "Used to GET the Time",
  		"DateTime": "Used to MANIPULATE the Date and Time",
  		"OS": "Used to interact with OS with provided functions",
  		"Glob": "Used to Find files by using WILDCARDS or Regular Expressions and returns them as a List",
  		"Sys": "????????????????????????",
  		"Re": "Uses Regular Expressions for Complex String Matching + String Manipulation",
  		"Urllib2": "Retrieves data from URLs",
  		"Smtplib": "Used to send mail to any Internet machine",
  		"Zlib": "Used for applications that need data compressed/decompressed",
  		"Unittest": "Provides functions for Unit Testing",
  		"Boto3": "Amazon Web Service SDK for Python to write software for S3 or EC2. Uses Object Oriented API + low level direct service access",
	}

	userImportOptions = []

	for index, importItem in enumerate(importDictionary):
		renamedImportFunctions = "importsExplanation._" + importItem.lower() + ("_import_Explanation()")
		userImportOptions.append(renamedImportFunctions)
		print('{:<3} {:<8} {:<3} {:<3}'.format(index + 1, importItem, " - ", importDictionary[importItem]))

	print(userImportOptions)

	userImportChoice = int(input("\nPlease select one for more info on the import and their functions:\n"))

	if userImportChoice <= (index):
		print("You selected: " + userImportOptions[userImportChoice - 1])
		exec(userImportOptions[userImportChoice - 1])

def math_Explanation():
	importsExplanation._math_import_Explanation()

def variables_and_names_Explanation():
	print("Python Variables are Typeless: They DON'T need to be Declared")
	print("They can be a:")
	print("#Int x = 123")
	print("#Long Int x = 123L")
	print("#String x = 'hello world'")
	print("#Double Float x = 3.14")
	print("#List x = [0,1,2,3,4]")
	print("#Tuple x = (0,1,2)")
	print("#File x = open('file.py', 'r')")
	
def strings_and_text_Explanation():
	print("Formatting strings:")
	print("%d - Replaces %d with the integer defined outside string")
	print("%s - Replaces %s with the variables or string defined outside string")
	print("%r - Prints the raw string(syntax to create string) rather than the result and its the Best Options for debugging: Look at code line 65-66 to understand more about raw string")
	print("\nx = 'There are %d types of people.' % 10")
	print("print (x) Should display: There are 10 types of people.\n")
	print("binary = 'binary'")
	print("do_not = 'don't'")
	print("y = 'Those who know %s and those who %s.' % (binary, do_not)")
	print("print (y) Should display: Those who know binary and those who don't.\n")
	print(r"z = 'Hello\nworld'")
	print(r"print (z) Should display: 'Hello\nworld'")
	print("\nhilarious = False")
	print("joke_evaluation = 'Isn't that joke so funny?! %r'")
	print("print (joke_evaluation % hilarious) Should display: Isn't that joke so funny?! False\n")
	print("a = 'Hello'")
	print("b = 'World'")
	print("print(a + b) Should Display: 'Hello World'\n")
	print("a = 'Hello'")
	print("b = 'World'")
	print("print('String Example:', a, b) Should Display: 'String Example: Hello World'\n")
	print("Common Escape Charachters/String Literals used in strings:")
	print(r"\n - Prints a new line wherever it's placed in string")
	print(r"\t - Prints a Tab in your string wherever you put it, Kinda like the start of a paragraph tab")
	print(r"\" - Prints Double Quotes in strings")
	print(r"\' - Prints Single Quotes in strings")
	print(r"\x(HexValue) - Converts and prints from Hex values into String")
	print(r"\(123)\(123)\(123) - Convert 3 digit values from Octal into String")
	print("Aligning Output using Str.Format:")

def functions_Explanation():
	print("Functions are basically Java Methods")
def api_Explanation():
	print("Here's a quick explanation about API")

def main():
	print("Python Concepts:")
	userFunctions = []
	userOptions = ['Commenting','Imports','Math','Variables and Names',
	'Strings and Text Formatting','User Input and Paramaters', 'Dictionary',
	'Reading Files', 'Writing Files', 'Functions', 'Boolean', 'Try Catch', 'Tips and Tricks', 'Debugging', 'API']

	for index, item in enumerate(userOptions):

		renamedItem = item.lower().replace(" ","_") + "_Explanation"
		userFunctions.append(renamedItem)
		print ('{:<3} {:<0}'.format(index + 1, item))

	try:
		userInput = int(input("\nPress select one of the options to learn more about these concepts:\n"))
		if userInput <= (index + 1):
			print("Here's the explanation for:", userOptions[userInput - 1] + "\n")
			#os.system('cls')
			globals()[userFunctions[userInput - 1]]() 
			#This will call one of the functions based on the string from the userFunctions list
			#globals() means it'll go through other python files to find your function
			#locals() will try to find your function in this file only
		else:
			userFunctions[userInput]
			print("Wrong: Over the Limit")
	except Exception as e:
		print("~~~~~~~~~~~~~~~~This isnt a proper number~~~~~~~~~~~~~~~~~~~~`", e)


if __name__ == "__main__":
	main()


#Create class/function names with the names of the concepts and when user input the number, itll activate the class/function name

#while True:
#    print("This prints once a minute.")
#    time.sleep(1) # Delay for 1 seconds

#Modules are python files with classes or functions
#Scripts are python files with classes and functions

#"Function" used insides file/module
#"_Function" used in another file/module

#def functionname
#def __init__ functioname ----------> for function to make objects

#Remember to explain WHEN to use a List, Array, or a Dictionary

#Remember to exolain string alignment