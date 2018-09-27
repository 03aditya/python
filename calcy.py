#mathematical operation using function and its condition
a=int(input("enter a number"))
b=int(input("enter another number:"))
c=int(input("which mathematical operation do you perform,+,-,x,/,?"))
def sub():
    print("substraction=")
    return a-b

def add():
	print("addition=")
	return a+b

   	
def mul():
	print("multiplication=")
	return a*b

def div():
    print("division=")
    return a/b
   
if(c=='+'):
	add()
elif(c=='-'):
	sub()
elif(c=='x'):
	mul()
elif(c=='/'):	
	div()


 