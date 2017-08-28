# this is test the asking dir function
# -*-coding: UTF-8 -*-

from tkinter import *
from tkinter import messagebox

import pygubu

from SOURCE.ResultsParser import *


class AnalysisResults():
    def __init__(self, master):
        self.builder = pygubu.Builder()
        self.builder.add_from_file("results.ui")
        self.win = self.builder.get_object("LabelFrame_1", master)

        self.builder.connect_callbacks(self)

        self.index = 0
        self.loadResults()

    def loadResults(self):
        self.result = ResultsParser().GetResults()[self.index]
        self.builder.get_variable("data_file_name").set(self.result.data_file_name)
        self.builder.get_variable("reliability_value").set(self.result.reliability)
        for i in range(10):
            self.builder.get_variable("v_bottle_neck_" + str(i + 1)).set(self.result.v_bottleneck[i])
            self.builder.get_variable("t_bottle_neck_" + str(i + 1)).set(self.result.t_bottleneck[i])
            self.builder.get_variable("l_bottle_neck_" + str(i + 1)).set(self.result.l_bottleneck[i])
            self.builder.get_object("Entry_" + str(3 + self.result.v_bottleneck_index)).configure(background="yellow")
            self.builder.get_object("Entry_" + str(13 + self.result.t_bottleneck_index)).configure(background="yellow")
            self.builder.get_object("Entry_" + str(23 + self.result.l_bottleneck_index)).configure(background="yellow")
        status = "现在正在读取第 " + str(self.index + 1) + " 个文件(共有10个文件）"
        self.builder.get_variable("status_label_text").set(status)

    def OnClickNextButton(self):
        if self.index == 9:
            messagebox.showinfo("警告", "最后一个文件！")
        else:
            self.index += 1
            self.loadResults()

    def OnClickLastButton(self):
        if self.index == 0:
            messagebox.showinfo("警告", "第一个文件！")
        else:
            self.index -= 1
            self.loadResults()


def main():
    root = Tk()
    root.title("Testing the Asking path")
    myAnalysis = AnalysisResults(root)
    root.mainloop()


if __name__ == "__main__":
    main()
