#Responding left,middle,right click buttons on window using function with event argument.

import tkinter
window=tkinter.Tk()
window.title("tkinter_python")

#creaing a function with event argument
def left_click(event):
	tkinter.Label(window,text="Leftclick!").pack()

def middle_click(event):
	tkinter.Label(window,text="Middleclick!").pack()

def right_click(event):
	tkinter.Label(window,text="Rightclick!").pack()

window.bind("<Button-1>",left_click)
window.bind("<Button-2>",middle_click)
window.bind("<Button-3>",right_click)

window.geometry("200x200")
window.mainloop()
