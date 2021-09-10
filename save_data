def main():
	contin = True
	f = open("list.txt", "a", newline='\n')
	f.write("begin \n")
	f.close()
	while contin:
		name = input('Name: ')
		age = input('Age: ')
		f = open('list.txt', 'a', newline='\n')
		f.write('#' + name)
		f.write('%')
		f.write(age)
		#f.write('#')
		f.close()
		more = input('Continue? (y/n): ')
		if more == 'n':
			f = open("list.txt", "a", newline='\n')
			f.write('\n')
			f.write("end \n")
			f.close()
			contin = False
	print('Good bye')

if __name__ == "__main__":
	main()
