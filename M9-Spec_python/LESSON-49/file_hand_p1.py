#open file and read its contents
file = open('C:\\Users\\samai\\OneDrive\\Documents\\Codingal_Learn\\webdev course\\MODULES\\M9-Spec_python\\LESSON-49\\codingal.txt','r')
print(file.read())
file.close()

#open file and read its beginning 8 characters
file = open('C:\\Users\\samai\\OneDrive\\Documents\\Codingal_Learn\\webdev course\\MODULES\\M9-Spec_python\\LESSON-49\\codingal.txt','r')
print("\n Read in parts \n")
print(file.read(8))
file.close()

#append your name and age in the file
file = open('C:\\Users\\samai\\OneDrive\\Documents\\Codingal_Learn\\webdev course\\MODULES\\M9-Spec_python\\LESSON-49\\codingal.txt','a')
file.write(" Hi! I am Penguin and I am 1 yr old.")
file.close()

