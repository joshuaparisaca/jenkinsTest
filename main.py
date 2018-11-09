import time
import math
import os
import datetime
import glob
import re

import importsExplanation

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
  		"Time": "GETS the Time",
  		"DateTime": "MANIPULATES the Date and Time",
  		"OS": "Interact with your current OS and its FOLDER/FILES",
  		"Sys": "Used to MANIPULATE Command Line arguements passed to python script",
  		"Glob": "Uses WILDCARDS to FIND FILES",
  		"Re": "Uses REGULAR EXPRESSIONS for String Matching + Manipulation",
  		"Urllib2": "ACCESS WEBSITES to return info",
  		"Smtplib": "Used to send mail to any Internet machine",
  		"Zlib": "COMPRESS/DECOMPRESS files and objects",
  		"Unittest": "Provides functions for Unit Testing",
  		"Boto3": "Amazon Web Service SDK for Python to write software for S3 or EC2. Uses Object Oriented API + low level direct service access",
	}

	userImportOptions = []

	for index, importItem in enumerate(importDictionary):
		renamedImportFunctions = "importsExplanation._" + importItem.lower() + ("_import_Explanation()")
		userImportOptions.append(renamedImportFunctions)
		print('{:<3} {:<8} {:<3} {:<3}'.format(index + 1, importItem, " - ", importDictionary[importItem]))

	print(userImportOptions)

	userImportChoice = eval(input("\nPlease select one for more info on the import and their functions:\n"))

	if userImportChoice <= (index):
		print("You selected: " + userImportOptions[userImportChoice - 1])
		exec(userImportOptions[userImportChoice - 1])

def variables_and_names_Explanation():
	print("Python Variables are Typeless: They DON'T need to be Declared")
	print("They can be a:")
	print("#Int x = 123")
	print("#Long Int x = 123L")
	print("#String x = 'hello world'")
	print("#Double Float x = 3.14")
	print("#List x = [0,1,2,3,4]")
	print("#Tuple x = (0,1,2)")
	print("#File x = open('file.py', 'r')\n")
	print("\nUse type() to determine what type of value a variable has")
	print("x = 5.3")
	print("type(x)")
	print("Result is:", type(5.3))
	print("\nGlobal, Local, NonLocal Variables:")
	print('{:<20} {:<15}'.format("Global variables:", "Variables that are declared OUTSIDE all functions and the main function"))
	print('{:<20} {:<15}'.format("Local variables:", "Variables that are declared INSIDE a function"))
	print('{:<20} {:<15}'.format("NonLocal variables:", "Variables that are declared in a nested function/function inside a function"))

def math_Explanation():
	importsExplanation._math_import_Explanation()

def strings_and_text_formatting_Explanation():
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
	# print("Aligning Output using Str.Format:")
	stringFunctionsDict = {
		"isalnum()":"Checks if string has BOTH letters AND numbers",
		"isdigit()":"Check if string HAS digits",
		"isalpha()":"Checks if string is alphabetical",
		"isupper()":"Checks if string is UPPERCASE",
		"islower()":"Checks if string is lowercase",
		"isspace()":"Checks if string is ONLY Spaces",
		"startswith(x)":"Checks if string starts with x",
		"endswith(x)":"Checks if string ends with x"
	}

	print("\nStrings functions that return TRUE/FALSE:")
	for item in stringFunctionsDict:
		print('{:<15} {:<15}'.format(item, stringFunctionsDict[item]))

def user_input_and_paramaters_Explanation():
	print("There's three ways to get user input:")
	print("input('>Enter user input:'): Will take input and convert it to a string")
	print("eval(input('>Enter user input')): Will take input and check if it's a int, float, or string and converts it to that")
	print("first, second, third = argv : DEMANDS that you put in 3 inputs before you execute the python file - needs the sys import")

def read_and_write_files_Explanation():

	fileFunctionsDict = {
		"open(filename)":"Opens a file",
		"read(filename)":"Reads a file that's been opened",
		"readline(filename)":"Reads ONLY ONE line of file",
		"write(filename)":"Writes OR Appends a file",
		"exists(filename)":"Checks if a file exists",
		"truncate(filename)":"EMPTIES content of a file",
		"filename.seek(x)":"Sets the file's current position,0 is start of file 2 is end of file",
		"close(filename)":"Closes/Saves a file and its changes"
	}

	for item in fileFunctionsDict:
		print('\t{:<20} {:<10}'.format(item, fileFunctionsDict[item]))

		matchObj = re.match( r'Writes OR Appends a file$', fileFunctionsDict[item])
		if matchObj:
			print("\t\tExample:")
			print("\t\tx = open(file.txt, a)")
			print("\t\tx.write('This line will APPEND to the file')")
			print("\t\ty = open(file.txt, w)")
			print("\t\ty.write('This line will OVERWRITE the file with this line. Can also use a file to overwrite another file')\n")

def functions_Explanation():
	print("Functions are basically Java Methods")
	print("These functions accept arguements/parameters and the last doesn't:\n")
	
	functionTypes = {
		"def function1(*args)" : "This function can take in UNLIMITED arguements/parameters/ Good to store and loop in a list",
		"def function2(args1)" : "This function needs ONE arguement/parameter to run",
		"def function3(args1, args2)" : "This function needs TWO arguements/parameters to run",
		"def function4()" : "This function DOES NOT need any arguement/parameters to run"
	}
	
	for item in functionTypes:
		print ('{:<28} {:<15}'.format(item, functionTypes[item]))

	print("\nThey can accept variables values")
	print("x = 4")
	print("def function(x)\n")
	print("They can accept direct string, int, lists, etc.")
	print("def function('Hello', 2.5, [2,3,6])\n")
	print("You can even calculate math inside them")
	print("def function(x + 4, 2 + 2)")

	print("\nHow Functions return values")
	print("def function1(a, b, c)")
	print("\tprint('Adding %d and %d and %d' % (a, b, c))")
	print("\treturn a + b + c\n")
	print("This how to return multiple values and store them in variables:")
	print("def function2(a, b, c)")
	print("\tprint('Look at these values: %d and %d and %d' % (a, b, c))")
	print("\treturn a, b, c")
	print("newvalue1, newvalue2, newvalue3 = function2(a, b, c)")

def conditionals_Explanation():

	comparisonDict = {
		"==":"Condition1 EQUALS Condition2",
		"!=":"Condition1 NOT EQUALS Condition2",
		"<>":"Condition1 NOT EQUALS Condition2",
		"<":"Less than ",
		"<=":"Less than or equal to",
		">":"Greater than",
		">=":"Greater than or equal to",
		"AND":"Condition1 AND Condition2 HAS to be TRUE",
		"OR":"Condition1 OR Condition2 CAN be TRUE",
		"NOT":"Returns TRUE if condition/bool variable/function is false",
		"TRUE":"If Function executes or Bool variable",
		"FALSE":"If Function fails or Bool variable"
	}
	
	for item in comparisonDict:
		print('{:<15} {:<10}'.format(item, comparisonDict[item]))

	print("\nx = 15")
	print("if x == 15:")
	print("\tprint('x is 15')")
	print("elif x < 15")
	print("\tprint('x less than or equal to 15')")
	print("elif x > 15")
	print("\tprint('x greater than or equal to 15')")
	print("else:")
	print("\tprint('x is NOT a number')")

def loops_Explanation():
	print("numberList = [1,2,3,4,5]")
	print("for item in numberList:")
	print("\tprint(item)")
	print("for x in range(0,6)")
	print("\tprint(x)")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")

def main():
	print("Python Concepts:")
	userFunctions = []
	userOptions = ['Commenting','Imports','Variables and Names', 'Math',
	'Strings and Text Formatting','User Input and Paramaters', 'Read and Write Files', 
	'Functions', 'Conditionals', 'Loops', 'Dictionary', 'Try Catch', 'Debugging', 'API']

	for index, item in enumerate(userOptions):
		renamedItem = item.lower().replace(" ","_") + "_Explanation"
		userFunctions.append(renamedItem)
		print ('{:<3} {:<0}'.format(index + 1, item))

	try:
		userInput = eval(input("\nPress select one of the options to learn more about these concepts:\n"))
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