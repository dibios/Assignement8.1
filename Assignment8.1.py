# File processing activieties program
# Import OS library
import os

def main():
	"""Choose a directory"""
	directory = input("Enter the directory in which you want to save your file: ")
	"""Choose your file name"""
	filename = input("Enter the filename: ")
	name = input("Enter your name: ")
	address = input("Enter your address: ")
	phone_number = input("Enter your phone number: ")

	#Check to see if the directory exist
	if os.path.isdir(directory):
		# Create and open the file to write to
		wFile = open(os.path.join(directory, filename), 'w')
		# Write the data by comma seperated
		wFile.write(name+','+address+','+phone_number+'\n')
		# Close the file when we are done
		wFile.close()

		print("Your information:")
		#Make sure the file is saved by reading it
		readFile = open(os.path.join(directory,filename),'r')
		for line in readFile:
			print(line)
		readFile.close()
	else:
		print ("Sorry, this directory does not exist ")
main()
