#Responding button using function with event argument.

import tkinter
window=tkinter.Tk()
window.title("tkinter_python")

#creaing a function with event argument
def say_hi(event):
	tkinter.Label(window,text="Hai user!").pack()

btn=tkinter.Button(window,text="click me!")

#bind takes 2 parameters,(1-event,2-function)
btn.bind("<Button-1>",say_hi)
btn.pack()


window.geometry("200x200")
window.mainloop()
