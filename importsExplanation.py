def _math_import_Explanation():
	print("Common Math Operators:")
	print("\t+  Addition")
	print("\t-  Subtraction")
	print("\t*  Mulitplication")
	print("\t/  Division")
	print("\t%  Module")
	print("\t<  Less Than")
	print("\t<= Less Than or Equal to")
	print("\t>  Great Than")
	print("\t>= Greater Than or Equal to\n")
	#print(math.isnan(y))

	mathFunctionDictionary = {
		"math.ceil(x)": "Rounds up the variables to the next integer",
		"floor(x)": "Rounds down the variables to the next integer",
		"fabs(x)": "Returns the Absolute value of x",
		"factorial(x)": "Returns the factorial of x",
		"fmod(x, y)": "Returns the remainder of X divided by Y",
		"fsum(List/Array)": "Finds the total sum of an Array/List",
		"isnan(x)": "Returns TRUE if X is NaN(Not a Number) | Returns False if X is actually a number",
		"pow(x, y)": "Returns X to the power of Y",
		"pi": "Returns the value of pi",
		"e": "Returns the value of e"
	}

	print("Math Import functions:")	
	for x in mathFunctionDictionary:
		print ('\t{:<18} {:<8}'.format(x, mathFunctionDictionary[x]))


def _time_import_Explanation():

	timeFunctionDict = {
		"time.time()":"Returns the CURRENT time as a floating point number and NEEDS to be inside another function to work properly",
		"localtime()":"Returns the local time from this second to month to year",
		"ctime()":"Displays the current time in this format: Tue Feb 17 09:42:58 2009 | Doesn't need time.locatime parameter",
		"asctime(time.localtime())":"Returns the current in this format: Tue Feb 17 09:42:58 2009 ",
		"sleep(x)":"Stop execution of application based on the number value of x, Good for slowing down while loops",
		"strftime(x)":"Converts a tuple of int values into a dateTime formatted string like: Feb 18 2009 00:03:38 | Gooogle How format it"
	}
	
	print("Time Import functions:")
	for x in timeFunctionDict:
		print ('\t{:<18} {:<8}'.format(x, timeFunctionDict[x]))

def _datetime_import_Explanation():

	dateTimeFunctionDict = {
		"datetime.date(YYYY,MM,DD)":"This returns the date specified by the user",
		"time(HH,MM,SS,MS,TZInfo)":"This will return the time specified by the user",
		"datetime(YYYY,MM,DD,HH,MM,SS,MS,TZInfo)":"This will return the Date + Time defined by the user",
		"replace(x,y,z)":"Overwrites the existing datetime variable with new values based on the variable's parameters",
		"date.today().strftime('%Y')":"Current year",
		"date.today().strftime('%B')":"Month of year",
		"date.today().strftime('%w')":"Weekday of the week",
		"date.today().strftime('%d')":"Day of the month",
		"date.today().strftime('%A')":"Day of week:",
	}

	for x in dateTimeFunctionDict:
		print(x , dateTimeFunctionDict[x])


def _os_import_Explanation():
	print("333333333333333333")
def _glob_import_Explanation():
	print("4444444444444444")
def _sys_import_Explanation():
	print("55555555555555555555555555")
def _re_import_Explanation():
	print("555566666666666666666666666666666666666666")
def _urllib2_import_Explanation():
	print("666666666666666666666666666666666")
def _smtplib_import_Explanation():
	print("66666666666666666666666666666666666666666666666666")
def _zlib_import_Explanation():
	print("6666666666666666666666666666666666666666666666666666666666666")
def _unittest_import_Explanation():
	print("6666666666666666666666666666666666666666666666")
def _boto3_import_Explanation():
	print("4444444444444444444444444444444444444444444444444")