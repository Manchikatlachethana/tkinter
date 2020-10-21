#basic login form with 2 labels,2 input fields and with one checkbutton.

import tkinter
window=tkinter.Tk()
window.title("LoginForm")

#this is placed in 0 row  0 column
tkinter.Label(window,text="Username").grid(row=0)

#Entry to display input field at  0 row,1 column
tkinter.Entry(window).grid(row=0,column=1)

#this is placed in 1 row  0 column
tkinter.Label(window,text="Password").grid(row=1)

#Entry to display input field at  1 row,1 column
tkinter.Entry(window).grid(row=1,column=1)

#checkbutton using columnspan,which takes width 2
tkinter.Checkbutton(window,text="keep me logged in").grid(columnspan=2)

window.mainloop()
