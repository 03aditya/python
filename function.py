#using functions

#reading the values
a=int(input("enter the value of a"))
b=int(input("enter the value of b"))


#defining addition
def add():
	return a+b
#defining substraction
def sub():
    print("substraction=")
    return a-b
s=sub()
print(s)

print("addition=")
r=add()
print(r)    	

def mul():
	print("multiplication=")
	return a*b
q=mul()
print(q)

def div():
    print("division=")
    return a/b
r=div()
print(r)    	