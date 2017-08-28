# this is for testing the function of showing the contents

import tkinter.filedialog as filedialog
import tkinter.scrolledtext as ScrolledText
from tkinter import *


class LoadFile:
    def __init__(self, master):
        frame = Frame(master, width=400, height=400)
        frame.pack()

        self.button = Button(frame, text="Choose a File...", command=self.chooseFile)
        self.button.pack(side=LEFT)
        self.textBox = ScrolledText.ScrolledText(frame, width=60)
        self.textBox.pack(side=BOTTOM, fill=BOTH)

    def chooseFile(self):
        file = filedialog.askopenfile()
        self.textBox.insert(INSERT, file.readlines())


def main():
    root = Tk()
    root.title("Testing the Open File")
    loadfile = LoadFile(root)
    root.mainloop()


if __name__ == "__main__":
    main()
