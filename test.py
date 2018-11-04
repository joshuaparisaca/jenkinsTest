import time
import os
import math

#Make sure to know how to define a global function

def commenting_Explanation():
	print("# Is used for a single line comment")
	print("'''")
	print("These 3 quotes will comment for multiple lines")
	print("''' \n")
	print("Both the SingleLine comment and MultiLine comment WILL NOT WORK if it's inside a string")

def math_Explanation():
	print("Common Math Operators:")
	print("+  Addition")
	print("-  Subtraction")
	print("*  Mulitplication")
	print("/  Division")
	print("%  Module")
	print("<  Less Than")
	print("<= Less Than or Equal to")
	print(">  Great Than")
	print(">= Greater Than or Equal to")
	print("")
	#print(math.isnan(y))
	print("Math Import functions:")	
	print("ceil(x): Rounds up the variables to the next integer.")	
	print("floor(x): Rounds down the variables to the next integer")	
	print("fabs(x): Returns the Absolute value of x")	
	print("factorial(x): Returns the factorial of x")	
	print("fmod(x, y): Returns the remainder of X divided by Y")	
	print("fsum(iterableList/Array): Finds the total sum of an Array/List")	
	print("isnan(x): Returns TRUE if X is NaN(Not a Number) | Returns False if X is actually a number")	
	print("pow(x, y: Returns X to the power of Y")	
	print("pi: Returns the value of pi")	
	print("e: Returns the value of e")	

def imports_Explanation():
	print("Most commonly used imports/libraries")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")

def variables_and_names_Explanation():
	print("This is a Variables and Names function")

def functions_Explanation():
	print("Functions are basically Java Methods")
def api_Explanation():
	print("Here's a quick explanation about API")

print("Run the following commands in git bash to push to Github repository:")
print("git add .")
print("git commit -m 'Commit Description'")
print("git push -u origin master\n")

print("Python Concepts:")
userFunctions = []
userOptions = ['Commenting','Imports','Math','Variables and Names',
'Strings and Text','Printing','Parameters and Input',
'Reading Files', 'Writing Files', 'Functions', 'Boolean', 'Try Catch', 'Tips and Tricks', 'Debugging', 'API']

for index, item in enumerate(userOptions):
	renamedItem = item.lower().replace(" ","_") + "_Explanation"
	userFunctions.append(renamedItem)
	print (index + 1, item)

try:
	userInput = int(input("\nPress select one of the options to learn more about these concepts:\n"))
	if userInput <= (index + 1):
		print("Here's the explanation for:", userOptions[userInput - 1] + "\n")
		os.system('cls')
		print(userFunctions[userInput - 1])
		globals()[userFunctions[userInput - 1]]() 
		#This will call one of the functions based on the string from the userFunctions list
		#globals() means it'll go through other python files to find your function
		#locals() will try to find your function in this file only
	else:
		userFunctions[userInput]
		print("Wrong: Over the Limit")
except Exception as e:
	print("~~~~~~~~~~~~~~~~This isnt a proper number~~~~~~~~~~~~~~~~~~~~`", e)


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

#Also check out the Python Library
