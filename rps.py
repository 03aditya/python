import random
while(True):
	a={1:"r",2:"p",3:"s"}
	u=input("enter a random valur from p,r,s")
	if(u=='p' or u=='r' or u=='s'):
		c=a[random.randint(1,3)]
		print("u choose",u,"computer choose",c)
		if(u==c):
			print("it is tie")
		elif((c=='r'and u=='p') or(c=='p'and u=='s') or (c=='s'and u=='r')):
			print("user is the winner")
		else:
			print("computer is the winner")		
	else:
		print("please enter a valid key")
		exit()
