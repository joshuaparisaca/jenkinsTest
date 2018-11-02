import time

print("Run the following commands in git bash to push to Github repository:")
print("git add .")
print("git commit -m 'Commit Description'")
print("git push -u origin master\n")
#Test Comment

print("Python Concepts:")
userOptions = ['Imports','Math','Variables and Names',
'Strings and Text','Printing','Parameters and Input',
'Reading Files', 'Writing Files', 'Functions', 'Boolean', 'Try Catch']

userFunctions = [imports(), math(), variables(), ...]

for index, item in enumerate(userOptions):
	print (index + 1, item)

try:
	userInput = int(input("\nPress select one of the options to learn more about these concepts:\n"))
	if userInput <= (index + 1):
		print("Correct: Under the Limit")
		print("You've chosen:", userOptions[userInput-1])
	else:
		userFunctions[userInput]
		print("Wrong: Over the Limit")
except Exception as e:
	print("This isnt a proper number ", e)


#Create class/function names with the names of the concepts and when user input the number, itll activate the class/function name

#while True:
#    print("This prints once a minute.")
#    time.sleep(1) # Delay for 1 seconds

#_Function used insides file/module
#function used in another file/module

#def functionname
#def __init__ functioname ----------> for function to make objects

#Also check out the Python Library