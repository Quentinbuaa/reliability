import os
import tkinter.filedialog as filedialog
from tkinter import *
from tkinter import messagebox

from SOURCE.ConfigFileIO import ConfigFile


class AskDir:
    def __init__(self, master, win_index):
        frame = Frame(master, width=400, height=400)
        frame.pack()

        self.paraKey = win_index
        self.paraValue = ""
        self.configFile = ConfigFile()

        self.v_entry = StringVar()
        self.entry = Entry(frame, textvariable=self.v_entry, width=60)
        self.entry.grid(sticky=W + N, row=0, column=0, columnspan=2, padx=5, pady=5)

        self.selectionButton = Button(frame, text="选择一个文件夹", command=self.chooseAFile)
        self.selectionButton.grid(sticky=W + N, row=1, column=0, padx=5, pady=5)
        self.confirmButton = Button(frame, text="确认", width=10, command=self.Confirm)
        self.confirmButton.grid(sticky=E + N, row=1, column=1, padx=5, pady=5)
        self.listbox = Listbox(frame, width=60)
        self.listbox.grid(sticky=W + N, row=2, column=0, columnspan=2, padx=5, pady=5)

    def chooseAFile(self):
        self.paraValue = filedialog.askdirectory()
        if self.paraValue:
            self.v_entry.set(self.paraValue)
            self.getFile()

    def getFile(self):
        files = os.listdir(self.paraValue)
        if len(files) > 0:
            index = 0
            for file in files:
                self.listbox.insert(index, file)
                index += 1

    def Confirm(self):
        try:
            if self.configFile.UpdateParameters(self.paraKey, self.paraValue):
                messagebox.showinfo("提示", "配置文件路径为：" + self.paraValue)
            else:
                messagebox.showinfo("提示", "配置文件路径与原始路径相同")
        except Exception as e:
            print(e)


def main():
    root = Tk()
    root.title("Testing the Asking path")
    askdir = AskDir(root, "data_dir")
    root.mainloop()


if __name__ == "__main__":
    main()
