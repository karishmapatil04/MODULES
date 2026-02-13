# Program to remove lines starting with any prefix
file1 = open('C:\\Users\\samai\\OneDrive\\Documents\\Codingal_Learn\\webdev course\\MODULES\\M9-Spec_python\\LESSON-49\\codingal.txt','r')
file2 = open('C:\\Users\\samai\\OneDrive\\Documents\\Codingal_Learn\\webdev course\\MODULES\\M9-Spec_python\\LESSON-49\\sample.txt','w')

# reading each line from original
# text file
for line in file1.readlines():
	
	# reading all lines that do not
	# begin with "Coding"
	if not (line.startswith('we')):
		
		# printing those lines
		print(line)
		
		# storing only those lines that
		# do not begin with "Coding"
		file2.write(line)

# close and save the files
file2.close()
file1.close()
