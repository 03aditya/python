import random

while True:

	i=input("enter 'r' to roll the dice amd 'q' to quit")
	if(i=='r'):
		print("you got",random.randint(1,6))
	if(i=='q'):
		print("thank you.catch you later!")
		exit()
    	
