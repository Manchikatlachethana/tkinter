import tkinter

window=tkinter.Tk()

#title for window
window.title("GUI") 

#label text
l1=tkinter.Label(window,text="welcome User,Enter your name!!",font=("ArialBold",40))
l1.grid(column=3,row=3)

#entry
txt=tkinter.Entry(window,width=10)
txt.grid(column=2,row=5)

#clicked function 
def clicked():
	res="hai "+txt.get()
	l1.configure(text=res)

#button
bt1=tkinter.Button(window,text="Enter",fg="green",command=clicked)
bt1.grid(column=3,row=5)

#window geometry function
window.geometry("1000x500")
window.mainloop()
