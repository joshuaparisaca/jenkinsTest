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
		"date.today().strftime('%A')":"Day of week"
	}

	print("DateTime import functions:")	
	for x in dateTimeFunctionDict:
		print('%40s %2s  %11s' % (x, " - " , dateTimeFunctionDict[x]))

def _os_import_Explanation():
	osFunctionDict = {
		"os.name()":"Will find out which OS you're running",
		"getcwd()":"Returns the Current Working Directory you're on",
		"environ.get('PATH')":"Will list out ALL enviroment variables",
		"abort()":"Will abort the application",
		"path.exists(x)":"Returns TRUE is file exist | FALSE otherwise",
		"listdir()":"Will list the files of the current directory",
		"mkdir(x)":"Will create a folder based on folder name",
		"makedirs(x/y)":"Will create a folder based on X value and a subfolder based on Y value",
		"chdir(filepath)":"Changes to a different filepath directory based on specified filepath",
		"rename(x,y)":"Will rename a x,filename with a new y,filename",
		"remove(x)":"Will delete a specified filename",
		"rmdir(x)":"Will delete a specified folder",
		"popen(x)":"A variable OS commandline arguement that will be executable once it's been read",
		"error()":"Is actually used in try/catch as 'except IOError' and will only activate trying to access a invalid or inaccessible file/filepath"
	}

	for x in osFunctionDict:
		print('\t{:<20} {:<8}'.format(x, osFunctionDict[x]))

def _glob_import_Explanation():
	globFunctionDict = {
		"glob.glob(x/filename)":"Uses Wildcards to return a list of files found",
		"iglob(x)":"Uses Wildcards to return a list of files found but stores them in memory",
		"escape(x)":"Finds filename but WILL IGNORE Glob Wildcards"
	}

	globWildcards = {
		"*":"*.txt matches all files with the txt extension",
		"/**/filename":"Will go through every subfolder recursively to find filename",
		"?":"??? matches files with 3 characters long",
		"[]":"[ABC]* matches files starting with A,B or C",
		"[..]":"[A..Z]* matches files starting with capital letters",
		"[!]":"	[!ABC]* matches files that do not start with A,B or C"
	}
	print("Glob import functions:")
	for x in globFunctionDict:
		print('\t{:<23} {:<15}'.format(x,globFunctionDict[x]))

	print("\nGlob Wildcards:")
	for x in globWildcards:
		print('\t{:<20} {:<10}'.format(x,globWildcards[x]))

def _sys_import_Explanation():
	sysFunctionDict = {
		"argv()":"Will return a list of command/parameters passed to this python script",
		"executable()":"Will return which python file is running",
		"stdout.write(x)":"Will print x",
		"stderr.write(x)":"Will print x in a error format",
		"stdin.readlines()":"Will ask user for console input",
		"path()":"Will return where the python modules are located",
		"exit()":"Exits the Python program"
	}

def _re_import_Explanation():
	reFunctionsDict = {
		"re.match(RegEx, x)":"Looks for Regular Expression at START of string",
		"search(RegEx, x)":"Looks for Regular Expression ANYWHERE in the string ",
		"sub(RegEx,RegEx,x)":"Replaces string found in Regular Expression with new Regular Expression",
		"split(RegEx,x)":"Gets substrings found in Regular expressions and splits them into a List",
		"findall(RegEx,y)":"Finds ALL SUBSTRINGS that matches the regular expression"
	}

	regularExpression = {
		"^The":"Matches any string that start with 'The'",
		"dog$":"Matches any string that ends in 'dog'",
		"^The dog$":"EXACTLY Matches any string that's 'The dog'",
		"abc+":"Matches 'ab' string that end with 1 or more 'c'",
		"abc*":"Matches 'ab' string that ends with 0 or any 'c'",
		"abc?":"Matches 'ab' string that ends with 0 or 1 'c'",
		"abc.":"Matches 'abc' and one extra character",
		"abc{2}":"Matches 'abc' is theres 2 extra 'c' at the end",
		"abc{2-5}":"Matches 'abc' if there 2 - 5 'c' at the end",
		"a(b|c)":"Matches either 'ab' or 'ac'",
		"a(bc){2,5}":"Matches either 'abcbc' or 'abcbcbcbcbc'",
		"[abc]":"Matches any string that has a, b, or c inside it",
		"[0-9]":"Matches any string that has 0-9 | Can be [\d]",
		"abc\s":"Matches 'abc' and white space or tab",
		"<.+?>":"Finds <div> and </div>. I dont know how and why",
	}
	print("Re import functions:")
	for x in reFunctionsDict:
		print('\t{:<20} {:<10}'.format(x,reFunctionsDict[x]))

	print("\nRegular Expressions breakdown:")
	for x in regularExpression:
		print('\t{:<20} {:<10}'.format(x,regularExpression[x]))

def _urllib2_import_Explanation():
	print("666666666666666666666666666666666")
	
def _smtplib_import_Explanation():
	print("66666666666666666666666666666666666666666666666666")

def _zlib_import_Explanation():
	zlibFunctionDict = {
		"compress(x, level = y)" : "This will compress your file based on int level [1 = Fast 9 = Slow but Best]",
		"compressobj()":"Compresses a HUGE file and returns a object to be used with compress()",
		"decompress(x)":"Will Decompress a compressed object/file"
	}

	print("ZLib Functions:")
	for x in zlibFunctionDict:
		print('\t{:<25} {:<10}'.format(x, zlibFunctionDict[x]))

def _unittest_import_Explanation():
	print("6666666666666666666666666666666666666666666666")

def _boto3_import_Explanation():
	print("4444444444444444444444444444444444444444444444444")