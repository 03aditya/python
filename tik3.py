a=['1','2','3','4','5','6','7','8','9']

def printboard():
	print(a[0],'|',a[1], '|',a[2])
	print("----------")
	print(a[3],'|',a[4], '|',a[5])
	print("----------")
	print(a[6],'|',a[7], '|',a[8])

p1 = True
while True:
	printboard()
	p=input("choose an available place : ")

	if p1:
		p=input("player 1, choose your place")
		if p in a:
			a[int(p)-1] = 'x'
			p1 = not p1

	else:
		p=input("player 2,choose your place : ")
		if p in a:
			a[int(p)-1] = '0'		
			p1 = not p1


	for i in(0,3,6):		
				if(a[i]==a[i-1] and a[i]==a[i+2]):
					print("game over")
					exit()
					for i in range(3):
						if(a[i]==a[i+3] and a[i]==a[i+6]):
							print("game over...")
							exit()		
				for i in range(3):
					if(a[i]==a[i+3] and a[i+6]):
						print("game over....")
						if(a[i]=='x'):
							print("congratulations to player 1")
						else:
							print("congratulations to player 2")
							printboard()
							exit()

				if(a[0]==a[4] and a[0]==a[8]):
					print("game over")
					if(a[4]=='x'):
						print("congratulations to player 1")
					else:
						print("congratulations to player 2")
						printboard()
						exit()

				if(a[2]==a[4] and a[2]==a[6]):
					print("game over")
					if(a[4]=='x'):
						print("congratulations to player 1")
					else:
						print("congratulations to player 2")
						printboard()							 				
						exit()
				else:
					print("you have entered an invalid position")
					continue	