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
    pass


if __name__ == "__main__":
    main()
