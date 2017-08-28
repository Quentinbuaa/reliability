# this is to test the json parser
# -*-coding: UTF-8 -*-

import json


class MyJsonIO:
    def __init__(self, configfilepath):
        self.jsonfilepath = configfilepath

    def WriteJson(self, source_data):
        with open(self.jsonfilepath, 'w', encoding='utf8') as f:
            json.dump(source_data, f, indent=4, ensure_ascii=False)

    def ReadJson(self):
        with open(self.jsonfilepath, 'r', encoding='utf8') as f:
            data = json.load(f)
        if not data == "":
            return data
        else:
            raise Exception("The json file is empty")


def main():
    myjson = MyJsonIO("test_WinConfigFile.json")
    source_data = {
        "data_button": {
            "text": "数据路径",
            "description": "选择数据路径按钮：数据路径中",
            "title": "数据路径选择"
        },
        "com_button": {
            "text": "代码路径",
            "description": "选择数据路径按钮：数据路径中",
            "title": "代码路径选择"
        },
        "tao_button": {
            "text": "Tao",
            "description": "选择数据路径按钮：数据路径中",
            "title": "Tao文件路径选择"
        },
        "fd_button": {
            "text": "软件失效密度",
            "description": "选择数据路径按钮：数据路径中",
            "title": "软件失效密度配置"
        },
        "fb_button": {
            "text": "软件失效比例",
            "description": "选择数据路径按钮：数据路径中",
            "title": "软件失效比例配置"
        },
        "confirm_button": {
            "text": "确认",
            "description": "选择数据路径按钮：数据路径中",
            "title": "确认"
        },
        "label_frame": {
            "text": "本窗口用于配置可靠性计算软件参数配置"
        }
    }
    myjson.WriteJson(source_data)


if __name__ == "__main__":
    main()
