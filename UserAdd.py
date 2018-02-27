#!/usr/bin/python

def func1(mystr):
	print(mystr)
	myname = input("name? ")
	myvar = input("age? ")
	if(myname == "pankaj" and myvar >= 0):
		print("correct - IF loop")
	elif(myname == "pandey - Elif loop"):
		print("theek")
	else:
		print("kutiya - Else")

func1("Hello fun1")