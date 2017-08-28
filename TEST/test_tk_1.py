from tkinter import *


class MyToolbar:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.grid(row=1, column=0)

        tool_1 = Button(self.frame, text="Save")
        tool_2 = Button(self.frame, text="Open")
        tool_1.pack(side=LEFT)
        tool_2.pack(side=LEFT)


class App:
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.grid(row=0, column=0)

        self.button = Button(
            self.frame, text="QUIT", fg="red", command=self.frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(self.frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print("hi there, everyone!")


root = Tk()
root.title("Reliability Test")
root.minsize(width=600, height=200)

mytoolbar = MyToolbar(root)
app = App(root)

v_1 = StringVar()
e_1 = Entry(root, textvariable=v_1)
e_1.grid(row=2, column=0)

v_2 = StringVar()
e_2 = Entry(root, textvariable=v_2)
e_2.grid(row=3, column=0)
e_1.focus()


def call_1():
    v_2.set(v_1.get())


b = Button(root, text="Cal", command=call_1).grid(row=4, column=0)

root.bind("<Return>", call_1)
root.mainloop()


# root.destroy() # optional; see description below
