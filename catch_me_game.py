#Try to click the button!

#importing libraries
from tkinter import *
from random import randint

#function which takes multiple arguments
def catch(*args):
	global row,column,b
	#initially row is 0 so it directly goes to else method.
	if row>230:
		row=randint(0,220)
	else:
		row=randint(240,440)
	#initially column is 0 so it directly goes to else method.
	if column>230:
		column=randint(0,220)
	else:
		column=randint(241,441)
	#button position
	b.place(x=row,y=column)


window=Tk()

#naming the window and geomertry
window.title("catch game") 
window.geometry('500x500')

#creating button
b=Button(window,text="catchme!")

#calling bind function which takes Enter event and function as parameters.
b.bind("<Enter>",catch)

#Initially row and column are set to 0
row=0
column=0
#setting the position of button using place function.
b.place(x=row,y=column)

window.mainloop()