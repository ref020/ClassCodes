from tkinter import *

window = Tk()

label1 = Label(window, text="a", bg="red", fg="white")
label1.pack(fill=X)

label2 = Label(window, text="b", bg="blue", fg="white")
label2.pack(fill=BOTH, expand=1)

label3 = Label(window, text="c", bg="green", fg="white")
label3.pack(fill=X)
