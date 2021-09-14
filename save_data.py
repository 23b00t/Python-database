def main():
	def intro():
		usrin = input('Do you want to read (r) or write (w) data? ')
		if usrin == 'w':
			wdata(True)
		elif usrin == 'r':
			rdata(True)
		else:
			print('Wrong input!')
	def wdata(contin):
		#contin = True
		#f = open("list.txt", "a", newline='\n')
		#f.write("begin \n")
		#f.close()
		while contin:
			name = input('Name: ')
			age = input('Age: ')
			f = open('list.txt', 'a', newline='\n')
			f.write('#' + name)
			f.write('%' + age)
			#f.write(age)
			#f.write('#')
			f.close()
			more = input('Continue? (y/n): ')
			if more == 'n':
				f = open("list.txt", "a", newline='\n')
				f.write('\n')
				#f.write("end \n")
				f.close()
				contin = False
		print('Good bye')
	def rdata(contin):
		f = open('list.txt')
		data = f.read()
		f.close()
		data = data.split('#')
		print(data)
		#print(type(data))
		while contin:
			usrin = input('To search for names press "n", to search for age press "a": ')
			if usrin == 'n':
				search = input('Name: ')
				#print(data)
				#print(type(data))
				for i in data:
					if search in i:
						print(i)
	intro()
if __name__ == "__main__":
	main()
