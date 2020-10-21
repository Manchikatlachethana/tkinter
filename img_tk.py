#displaying image using PhotoImage method.

import tkinter
window=tkinter.Tk()
window.title("tkinter_python")

#taking image from the directory and storing source in a variable.
icon=tkinter.PhotoImage(file="/Users/chethanamanchikatla/Desktop/tkinter/hello_tkinter_cartoon.png")

#displaying picture using a label by passing the picture variable to image parameter.
label=tkinter.Label(window,image=icon).pack()

window.mainloop()