# this is for testing the main window function
# -*- coding: UTF-8 -*-

import tkinter.scrolledtext as ScrolledText
from tkinter import *

from TEST.test_ask_dir import AskDir
from TEST.test_configure import Configure


class MainWin:
    def __init__(self, master):
        frame = Frame(master, width=800, height=800)
        frame.pack()
        button_width = 20
        self.dataButton = Button(frame, width=button_width, text="数据路径")
        self.comlineButton = Button(frame, width=button_width, text="代码行数路径")
        self.taoButton = Button(frame, width=button_width, text="Tao")
        self.fdButton = Button(frame, width=button_width, text="软件失效密度")
        self.fbButton = Button(frame, width=button_width, text="软件失效比例")

        self.dataButton.grid(column=0, row=0, sticky=E + N, padx=5, pady=5)
        self.comlineButton.grid(column=0, row=1, sticky=E + N, padx=5, pady=5)
        self.taoButton.grid(column=0, row=2, sticky=E + N, padx=5, pady=5)
        self.fdButton.grid(column=0, row=3, sticky=E + N, padx=5, pady=5)
        self.fbButton.grid(column=0, row=4, sticky=E + N, padx=5, pady=5)

        self.labelframe = ScrolledText.ScrolledText(frame, width=50, height=20, borderwidth=2, relief="groove")
        self.labelframe.insert(INSERT, "This is for parameter configuration ")
        self.labelframe.grid(column=1, row=0, rowspan=5, sticky=W, padx=5, pady=5)
        self.labelframe.configure(state=DISABLED)

        self.dataButton.bind('<Enter>', self.OnEnter)
        self.dataButton.bind('<Leave>', self.OnLeave)
        self.dataButton.bind('<Button-1>', self.OnClick)

        self.comlineButton.bind('<Enter>', self.OnEnter)
        self.comlineButton.bind('<Leave>', self.OnLeave)
        self.comlineButton.bind('<Button-1>', self.OnClick)

        self.fdButton.bind('<Enter>', self.OnEnter)
        self.fdButton.bind('<Leave>', self.OnLeave)
        self.fdButton.bind('<Button-1>', self.OnClick)

        self.fbButton.bind('<Enter>', self.OnEnter)
        self.fbButton.bind('<Leave>', self.OnLeave)
        self.fbButton.bind('<Button-1>', self.OnClick)

        self.taoButton.bind('<Enter>', self.OnEnter)
        self.taoButton.bind('<Leave>', self.OnLeave)
        self.taoButton.bind('<Button-1>', self.OnClick)

    def UpdateText(self, description):
        self.labelframe.configure(state='normal')
        self.labelframe.delete(1.0, END)
        self.labelframe.insert(END, description)
        self.labelframe.configure(state=DISABLED)

    def OnEnter(self, event):
        butt_text = event.widget.cget("text")
        if butt_text == "数据路径":
            self.dataButton.configure(background="yellow")
            self.UpdateText("HH")
            return 0
        if butt_text == "代码行数路径":
            self.comlineButton.configure(background="yellow")
            self.UpdateText("comcom")
            return 0
        if butt_text == "Tao":
            self.taoButton.configure(background="yellow")
            self.UpdateText("tao configuration")
            return 0
        if butt_text == "软件失效密度":
            self.fdButton.configure(background="yellow")
            self.UpdateText("failure density configuration")
            return 0
        if butt_text == "软件失效比例":
            self.fbButton.configure(background="yellow")
            self.UpdateText("failure proportion configuration")
            return 0

    def OnLeave(self, event):
        butt_text = event.widget.cget("text")
        if butt_text == "数据路径":
            self.dataButton.configure(background="SystemButtonFace")
            self.UpdateText("This is for parameter configuration")
            return 0
        if butt_text == "代码行数路":
            self.comlineButton.configure(background="SystemButtonFace")
            self.UpdateText("This is for parameter configuration")
            return 0
        if butt_text == "Tao":
            self.taoButton.configure(background="SystemButtonFace")
            self.UpdateText("This is for parameter configuration")
            return 0
        if butt_text == "软件失效密度":
            self.fdButton.configure(background="SystemButtonFace")
            self.UpdateText("This is for parameter configuration")
            return 0
        if butt_text == "软件失效比例":
            self.fbButton.configure(background="SystemButtonFace")
            self.UpdateText("This is for parameter configuration")
            return 0

    def OnClick(self, event):
        t = Toplevel(event.widget)
        t.grab_set()
        t.resizable(width=False, height=False)
        butt_text = event.widget.cget("text")
        if butt_text == "Data Dir":
            t.title("Data directory selection")
            data_askdir = AskDir(t)
            return 0
        if butt_text == "Code Lines":
            t.title("Code lines directory selection")
            comline_askdir = AskDir(t)
            return 0
        if butt_text == "Tao":
            t.title("Tao directory selection")
            tao_askdir = AskDir(t)
            return 0
        if butt_text == "Failure Density":
            t.title("Failure density configuration")
            fd_config = Configure(t)
            return 0
        if butt_text == "Failure Proportion":
            t.title("Failure proportion configuration")
            fb_config = Configure(t)
            return 0


def main():
    root = Tk()
    root.title("Configuration Window")
    root.resizable(width=False, height=False)
    mainWin = MainWin(root)
    root.mainloop()


if __name__ == "__main__":
    main()
