import time

def imports_Explanation():
	print("This an Import function")

def math_Explanation():
	print("This is a Math function")	

def variables_and_names_Explanation():
	print("This is a Variables and Names function")

def functions_Explanation():
	print("Functions are basically Java Methods")

print("Run the following commands in git bash to push to Github repository:")
print("git add .")
print("git commit -m 'Commit Description'")
print("git push -u origin master\n")

print("Python Concepts:")
userFunctions = []
userOptions = ['Imports','Math','Variables and Names',
'Strings and Text','Printing','Parameters and Input',
'Reading Files', 'Writing Files', 'Functions', 'Boolean', 'Try Catch']

for index, item in enumerate(userOptions):
	renamedItem = item.lower().replace(" ","_") + "_Explanation"
	userFunctions.append(renamedItem)
	print (index + 1, item)

try:
	userInput = int(input("\nPress select one of the options to learn more about these concepts:\n"))
	if userInput <= (index + 1):
		print("Correct: Under the Limit")
		print("You've chosen:", userOptions[userInput - 1])
		print(userFunctions[userInput - 1])
		globals()[userFunctions[userInput - 1]]() #This will call one of the functions based on the string from the userFunctions list
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
