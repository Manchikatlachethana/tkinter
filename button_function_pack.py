#Responding button using function.

import tkinter
window=tkinter.Tk()
window.title("tkinter_python")

#creaing a function called say_hi
def say_hi():
	tkinter.Label(window,text="Hai user!").pack()

tkinter.Button(window,text="click me!",command=say_hi).pack()
window.geometry("200x200")

window.mainloop()
