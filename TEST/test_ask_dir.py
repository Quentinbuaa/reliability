# this is test the asking dir function
# -*-coding: UTF-8 -*-

import os
import tkinter.filedialog as filedialog
from tkinter import *


class AskDir:
    def __init__(self, master):
        frame = Frame(master, width=400, height=400)
        frame.pack()

        self.entry = Entry(frame, width=60)
        self.entry.grid(sticky=W + N, row=0, column=0, columnspan=4, padx=5, pady=5)

        self.button = Button(frame, text="选择一个文件夹", command=self.chooseAFile)
        self.button.grid(sticky=W + N, row=1, column=0, padx=5, pady=5)
        self.listbox = Listbox(frame, width=60)
        self.listbox.grid(sticky=W + N, row=2, column=0, padx=5, pady=5)

    def chooseAFile(self):
        filepath = filedialog.askdirectory()
        if filepath:
            self.entry.insert(0, filepath)
            self.getFile(filepath)

    def getFile(self, filepath):
        files = os.listdir(filepath)
        if len(files) > 0:
            index = 0
            for file in files:
                self.listbox.insert(index, file)
                index += 1


def main():
    root = Tk()
    root.title("Testing the Asking path")
    askdir = AskDir(root)
    root.mainloop()


if __name__ == "__main__":
    main()
