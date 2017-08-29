# this is for testing the main window function
# -*- coding: UTF-8 -*-

import tkinter.scrolledtext as ScrolledText

from SOURCE.AnalysisResultsWindow import *
from SOURCE.AskDirWindow import AskDir
from SOURCE.ConfigParaWindow import Configure
from SOURCE.JsonFileIO import MyJsonIO


class MainWin:
    def __init__(self, master):
        frame = Frame(master, width=800, height=800)
        frame.pack()
        button_width = 20
        self.jsonConfigData = MyJsonIO("SOURCE/WinConfigFile.json").ReadJson()

        self.dataButton = Button(frame, width=button_width, text=self.jsonConfigData["data_button"]["text"])
        self.comlineButton = Button(frame, width=button_width, text=self.jsonConfigData["com_button"]["text"])
        self.taoButton = Button(frame, width=button_width, text=self.jsonConfigData["tao_button"]["text"])
        self.fdButton = Button(frame, width=button_width, text=self.jsonConfigData["fd_button"]["text"])
        self.fbButton = Button(frame, width=button_width, text=self.jsonConfigData["fb_button"]["text"])

        self.confirmButton = Button(frame, width=button_width, text=self.jsonConfigData["confirm_button"]["text"],
                                    relief="raise")

        self.dataButton.grid(column=0, row=0, sticky=E + N, padx=5, pady=5)
        self.comlineButton.grid(column=0, row=1, sticky=E + N, padx=5, pady=5)
        self.taoButton.grid(column=0, row=2, sticky=E + N, padx=5, pady=5)
        self.fdButton.grid(column=0, row=3, sticky=E + N, padx=5, pady=5)
        self.fbButton.grid(column=0, row=4, sticky=E + N, padx=5, pady=5)
        self.confirmButton.grid(column=0, row=5, sticky=E + N, padx=5, pady=5)

        self.labelframe = ScrolledText.ScrolledText(frame, width=50, height=20, borderwidth=2, relief="groove")
        self.labelframe.text = self.jsonConfigData["label_frame"]["text"]
        self.labelframe.insert(INSERT, self.labelframe.text)
        self.labelframe.grid(column=1, row=0, rowspan=6, sticky=W, padx=5, pady=5)
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

        self.confirmButton.bind('<Enter>', self.OnEnter)
        self.confirmButton.bind('<Leave>', self.OnLeave)
        self.confirmButton.bind('<Button-1>', self.OnClick)

    def UpdateText(self, description):
        self.labelframe.configure(state='normal')
        self.labelframe.delete(1.0, END)
        self.labelframe.insert(END, description)
        self.labelframe.configure(state=DISABLED)

    def OnEnter(self, event):
        butt_text = event.widget.cget("text")
        if butt_text == self.jsonConfigData["data_button"]["text"]:
            self.dataButton.configure(background="yellow")
            self.UpdateText(self.jsonConfigData["data_button"]["description"])
            return 0
        if butt_text == self.jsonConfigData["com_button"]["text"]:
            self.comlineButton.configure(background="yellow")
            self.UpdateText(self.jsonConfigData["com_button"]["description"])
            return 0
        if butt_text == self.jsonConfigData["tao_button"]["text"]:
            self.taoButton.configure(background="yellow")
            self.UpdateText(self.jsonConfigData["tao_button"]["description"])
            return 0
        if butt_text == self.jsonConfigData["fd_button"]["text"]:
            self.fdButton.configure(background="yellow")
            self.UpdateText(self.jsonConfigData["fd_button"]["description"])
            return 0
        if butt_text == self.jsonConfigData["fb_button"]["text"]:
            self.fbButton.configure(background="yellow")
            self.UpdateText(self.jsonConfigData["fb_button"]["description"])
            return 0
        if butt_text == self.jsonConfigData["confirm_button"]["text"]:
            self.confirmButton.configure(background="green")
            self.UpdateText(self.jsonConfigData["confirm_button"]["description"])
            return 0

    def OnLeave(self, event):
        butt_text = event.widget.cget("text")
        if butt_text == self.jsonConfigData["data_button"]["text"]:
            self.dataButton.configure(background="SystemButtonFace")
            self.UpdateText(self.labelframe.text)
            return 0
        if butt_text == self.jsonConfigData["com_button"]["text"]:
            self.comlineButton.configure(background="SystemButtonFace")
            self.UpdateText(self.labelframe.text)
            return 0
        if butt_text == self.jsonConfigData["tao_button"]["text"]:
            self.taoButton.configure(background="SystemButtonFace")
            self.UpdateText(self.labelframe.text)
            return 0
        if butt_text == self.jsonConfigData["fd_button"]["text"]:
            self.fdButton.configure(background="SystemButtonFace")
            self.UpdateText(self.labelframe.text)
            return 0
        if butt_text == self.jsonConfigData["fb_button"]["text"]:
            self.fbButton.configure(background="SystemButtonFace")
            self.UpdateText(self.labelframe.text)
            return 0
        if butt_text == self.jsonConfigData["confirm_button"]["text"]:
            self.confirmButton.configure(background="SystemButtonFace")
            self.UpdateText(self.labelframe.text)
            return 0

    def OnClick(self, event):
        self.OnEnter(event)
        t = Toplevel(event.widget)
        t.grab_set()
        t.resizable(width=False, height=False)
        butt_text = event.widget.cget("text")
        if butt_text == self.jsonConfigData["data_button"]["text"]:
            t.title(self.jsonConfigData["data_button"]["title"])
            data_askdir = AskDir(t, "data_dir")
            return 0
        if butt_text == self.jsonConfigData["com_button"]["text"]:
            t.title(self.jsonConfigData["com_button"]["title"])
            comline_askdir = AskDir(t, "com_dir")
            return 0
        if butt_text == self.jsonConfigData["tao_button"]["text"]:
            t.title(self.jsonConfigData["tao_button"]["title"])
            tao_askdir = AskDir(t, "tao_dir")
            return 0
        if butt_text == self.jsonConfigData["fd_button"]["text"]:
            t.title(self.jsonConfigData["fd_button"]["title"])
            fd_config = Configure(t)
            return 0
        if butt_text == self.jsonConfigData["fb_button"]["text"]:
            t.title(self.jsonConfigData["fb_button"]["title"])
            fb_config = Configure(t)
            return 0
        if butt_text == self.jsonConfigData["confirm_button"]["text"]:
            t.title(self.jsonConfigData["confirm_button"]["title"])
            result_window = AnalysisResults(t)
            return 0


def mainWindow():
    root = Tk()
    root.title("配置参数")
    root.resizable(width=False, height=False)
    mainWin = MainWin(root)
    root.mainloop()


def main():
    mainWindow()


if __name__ == "__main__    ":
    main()
