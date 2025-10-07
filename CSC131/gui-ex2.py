from tkinter import *

class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.button1 = Button(master, text="bye, bitch", fg="red", command=self.quit)
        self.button1.pack(side=LEFT)

        self.button2 = Button(master, text="say something", command=self.say)
        self.button2.pack(side=LEFT)

    def say(self):
        print("Something")
        self.button1.config(text="something", fg="blue")

window = Tk()
app =  App(window)
window.mainloop()
