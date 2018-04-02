# program3 - Program that will open a file and analysis the information. The program will determine 
#            the number of characters, lines and words and print out the value to the screen.
# Name: Brian Inglis
# WSU ID: a934z975

def main():
	user_file = input("Please enter the name of the file: ")
	infile = open(user_file + ".txt", "r")
	chars = 0 
	lines = 0
	words = 0
	for line in infile:
		list = line.split()
		lines += 1
		words += len(list)
		chars += len(line)
	print("The number of lines in the file is", lines)
	print("The number of words in the file is", words)
	print("The number of characters in the file is", chars)
	infile.close()
main()