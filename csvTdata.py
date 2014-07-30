'''
csvTdata reads data from a CSV file and displays Trend data sets
Author: Jason Bevis (conmigr@gmail.com) | infosecalways.com
Version: 0.2
Command Syntax: /python csvTdata.py <filename>

Changelog:
0.1
[+] Tool created
0.2
[+] Command line arguments and additional features added

To-Do
[ ] Color headers of terminal output
[ ] Count per string the number of events in a column
[ ] Print output in html file format
'''

import collections, csv, sys, argparse

def main():

	parser = argparse.ArgumentParser(description='csvTData reads data from a CSV file and displays Trend data sets')
	parser.add_argument('src', type=argparse.FileType('r'), default=sys.stdin)
	parser.add_argument("-s", "--sval", help="searches a string and provides trends", action="store", dest="sval")
	
	if len(sys.argv)==1:
		parser.print_help()
		sys.exit(1)
	args = parser.parse_args()

	# Identifies the columns to be used for trending
	'''Replace the current csv columns with your csv's column headers that you want to parse; Make sure to globally replace each column throughout the script by doing a find and replace on each column name.  Add additional columns and funcationality as needed'''
	Selected_Columns = ('acolumn','bcolumn','ccolumn','dcolumn')
	
	# Opens the csv file
	f = args.src

	# Define each item 'a,b,c,d' as its own counter using the collections module
	a = collections.Counter()
	b = collections.Counter() 
	c = collections.Counter()
	d = collections.Counter()

	# Define a dictionary for one of the selected columns in the Excel (bcolumn)
	bcolumn_data = dict()
	try:
	   # Creates the reader object
		reader = csv.reader(f)
			
		# Sets the tuple based on the Selected_Columns
		headers = None
		csvfields = []
			
		# For each row in reader if the header doesn't exist appeand the header column
		for row in reader:
			current_row=row
			if not headers:
				# creates a dummy_var= ""
				headers = []
				# for (i in headers) the col_val = current_row[i];
				for i, col in enumerate(row):
					if col in Selected_Columns:
					# Store the index of the cols of interest by dummy_var.append(col_val)
						headers.append(i)
			else:
				# csvfields.append(dummy_var); Enter a For Loop execution - Iteration #1 where Only the header is filled then For Loop execution - Iteration #2 csvfields has 1 row containing only the fields we are interested in then For Loop execution, etc.
				csvfields.append(tuple([row[i] for i in headers]))
	
				# Assigns a temp variable for the selected excel column (bcolumn) and maps another column to it
				bcolumn_temp=current_row[1]
				acolumn_temp=current_row[0]

				# This leverages a dictionary to map more than one column of data when output is displayed
				if bcolumn_temp in bcolumn_data:
					existing_bcolumn=bcolumn_data[bcolumn_temp]
					if acolumn_temp not in existing_bcolumn:
						bcolumn_data[bcolumn_temp]=existing_bcolumn + "," + acolumn_temp 
				else:
					bcolumn_data[bcolumn_temp]=acolumn_temp 
		
		# Each field in the csv is counted 
		for aTuple in csvfields: 
			acolumn = aTuple[0]
			a[acolumn] += 1
			bcolumn = aTuple[1] 
			b[bcolumn] += 1	 
			# The if statements below are examples to clean up output if the values include junk 
			ccolumn = aTuple[2]
			if len(ccolumn) < 7:
				c[ccolumn] += 1
			dcolumn = aTuple[3]
			if dcolumn != '':
				d[dcolumn] += 1

	# Counts the Column 'a' Values
		print '\n'
		print '--Number_of_Column_a_Values--'
		print 'ITEM           		 COUNT'
		for acolumn, count in a.iteritems():
			if len(acolumn) != 0:
				print '%s %5d' % (acolumn.ljust(20), count) 
						
		# Counts the Column 'b' Values
		print '\n'
		print '--Number_of_Column_b_Values'
		print 'ITEM                    COUNT TYPE'
		for bcolumn, count in b.iteritems():
		# Cleans up output to display only items which are over 5 characters
			if len(bcolumn) > 3: 
				print '%s %4d     %s' % (bcolumn.ljust(20), count, bcolumn_data[bcolumn])
				
		# Displays the top 10 most common Column 'c' Values	
		print '\n' 
		print '--Top_10_Column_c_Values'
		print 'ITEM                     COUNT'
		for ccolumn, count in c.most_common(20): 
			print '%s %5d' % (ccolumn.ljust(20), count)
		
		# Displays the top 10 most common 'd' Values
		print '\n' 
		print '--Top_10_Column_d_Values'	
		print 'ITEM                          COUNT'		
		for dcolumn, count in d.most_common(10): 
			print '%s %5d' % (dcolumn.ljust(25), count) 

		# Prints the total number of unique values for each column			
		print '\n'
		print 'The total unique column c values are: %d' % len(c)
		print 'The total unique column d values are: %d' % len(d)

		# Prints the sum total of items in a column	
		totalc = sum(c.values())
		print 'The total number of column c items is: %d' % totalc

		# This item leverages the command line arguement and prints a specific set of trends for the search value string that is entered and associated with one column.  In this case csv column 2(e.g. bcolumn)
		print '\n' 
		for bcolumn, count in b.iteritems():
			if bcolumn == args.sval:
				print '--sval Search String--'
				print 'STRING                       COUNT TYPE'
				print '%s %4d     %s' % (bcolumn.ljust(25), count, bcolumn_data[bcolumn])		
				
	finally:
		# Closes the file
		f.close() 

if __name__ == '__main__':
	main()
	
