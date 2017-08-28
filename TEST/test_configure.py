# this is to test the configuration function
# -*- coding: UTF-8 -*-

from tkinter import *


class Configure:
    def __init__(self, master):
        frame = Frame(master, width=400, height=400)
        frame.pack()

        self.fdLabel = Label(frame, text="软件失效密度:")
        self.fdLabel.grid(sticky=E + N, row=0, column=0, padx=5, pady=5)

        self.fbLabel = Label(frame, text="软件失效比例:")
        self.fbLabel.grid(sticky=E + N, row=1, column=0, padx=5, pady=5)

        self.v_fdEntry = StringVar()
        self.fdEntry = Entry(frame, textvariable=self.v_fdEntry)
        self.fdEntry.grid(sticky=E + N, row=0, column=1, padx=5, pady=5)
        self.v_fdEntry.set("1")

        self.v_fbEntry = StringVar()
        self.fbEntry = Entry(frame, textvariable=self.v_fbEntry)
        self.fbEntry.grid(sticky=E + N, row=1, column=1, padx=5, pady=5)
        self.v_fbEntry.set("0.000001")

        self.confirmButton = Button(frame, text="确认", width=10, command=self.confirm)
        self.confirmButton.grid(sticky=E + N, row=2, column=0, columnspan=2, padx=5, pady=5)

    def confirm(self):
        pass


def main():
    root = Tk()
    root.title("Testing the Open File")
    configure = Configure(root)
    root.mainloop()


if __name__ == "__main__":
    main()
