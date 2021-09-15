def main():
	def intro():
		usrin = input('''Do you want to read (r) or write (w) data? 
To exit press (e) : ''')
		if usrin == 'w':
			wdata(True)
		elif usrin == 'r':
			rdata(True)
		elif usrin == 'e':
			print('Good bye!')
		else:
			print('Wrong input!')
	def wdata(contin):
		while contin:
			name = input('Name: ')
			age = input('Day of birth (DD.MM.YYYY): ')
			adress = input('Adress: ')
			f = open('list.txt', 'a', newline='\n')
			f.write('#' + name)
			f.write('%' + age)
			f.write('%' + adress)
			f.close()
			more = input('Continue? (y/n): ')
			if more == 'n':
				f = open("list.txt", "a", newline='\n')
				f.write('\n')
				f.close()
				contin = False
			elif more == 'y':
				contin = True
			else:
				print('Wrong input')
				f = open("list.txt", "a", newline='\n')
				f.write('\n')
				f.close()
				contin = False
				intro()
		print('Good bye')
	def rdata(contin):
		f = open('list.txt')
		data = f.read()
		f.close()
		data = data.split('#')
		while contin:
			search = input('Search for name, day of birth or adress (open search): ')
			for i in data:
				if search.lower() in i.lower():
					#name = i.rstrip('1234567890%\n')
					#age = i.lstrip('abcdefghijklmnopqrstuvwxyzöäüzABCDEFGHIJKLMNOPQRSTUVWXYZÖÄÜß- %\n')
					singelData = i.split('%')
					print('Name:', singelData[0])
					print('Day of birth:', singelData[1])
					print('Adress:', singelData[2])
			usrin = input('Continue searching? (y/n) ')
			if usrin == 'y':
				contin = True
			elif usrin == 'n':
				contin = False
			else:
				print('Wrong input')
				contin = False
				intro()
	intro()
if __name__ == "__main__":
	main()
