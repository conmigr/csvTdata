'''
csvTdata reads data from a CSV file and displays Trend data sets
Author: Jason Bevis (conmigr@gmail.com) | infosecalways.com
Version: 0.1
Command Syntax: /python csvTdata.py <filename>

Changelog:
0.1
[+] Tool created

To do:
[-] Ability to parsing columns with newlines within double quotes (e.g. GET /)
'''

import collections, csv, sys

# Opens the csv file
# An array representing the 1st cmd line argument (as a string) is supplied to the script 
# Reads 'r' in binary 'b' mode 
f = open(sys.argv[1], 'rb')

# Define each item 'a,b,c,d' as its own counter using the collections module
a = collections.Counter()
b = collections.Counter() 
c = collections.Counter()
d = collections.Counter()

try:
    # Creates the reader object
	reader = csv.reader(f) 
	# Skips header row
	reader.next()

	for line in f: 
		# Lists the fields and strips the return and newline values for cleaner processing
		# Also splits the string based on the ',' separator value
		listoffields = line.replace('\r\n','').strip('\r\n').split(',') 	
	
		# If there are less than Nnumber fields (number of total csv fields) 
		# then we are not on a valid entry because of a possible line break or split
		if len(listoffields) < 8:
			continue  
		acolumn = listoffields[0]
		a[acolumn] += 1
		bcolumn = listoffields[1]
		# The if statements below are examples to clean up output if the values include junk 
		if len(bcolumn) > 7: 
			b[bcolumn] += 1	 
		ccolumn = listoffields[2]
		if len(ccolumn) != 0:
			c[ccolumn] += 1
		dcolumn = listoffields[3]
		if dcolumn != None and len(dcolumn) > 0: 
			d[dcolumn] += 1 
	
	# Counts the Column 'a' Values
	print '\n'
	print '--Number_of_Column_a_Values'
	for acolumn, count in a.iteritems():
		print '%s: %5d' % (acolumn, count) 

	# Counts the Column 'b' Values
	print '\n'
	print '--Number_of_Column_b_Values'
	for bcolumn, count in b.iteritems():
		print '%s: %5d' % (bcolumn, count) 
			
	# Displays the top 10 most common Column 'c' Values	
	print '\n' 
	print '--Top_10_Column_c_Values'
	for ccolumn, count in c.most_common(10): 
		print '%s: %5d' % (ccolumn, count)
	
	# Displays the top 10 most common 'd' Values
	print '\n' 
	print '--Top_10_Column_d_Values'			
	for dcolumn, count in d.most_common(10): 
		print '%s: %5d' % (dcolumn, count) 

	# Prints the total number of unique values for each column			
	print '\n'
	print 'The total unique column c values are: %d' % len(c)
	print 'The total unique column d values are: %d' % len(d)

	# Prints the sum total of items in a column	
	totalc = sum(c.values())
	print 'The total number of column c items is: %d' % totalc

finally:
    # Closes the file
	f.close() 

	



	