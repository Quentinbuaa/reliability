# Testing the function of convert parameters
# -*-coding: UTF-8 -*-

import os
import os.path
import re


class ConfigFile:
    def __init__(self):
        try:
            self.workdir = os.getcwd()
            self.configfilepath = os.path.join(self.workdir, "config.txt")
            self.parameters = {}
            self.ParaInitialization()
            self.isParaModified = False
        except Exception as e:
            print(e)

    def ParaInitialization(self):
        if not os.path.isfile(self.configfilepath):
            raise Exception("Func ParaInitialization, config.txt is not exist")
        else:
            with open(self.configfilepath) as fr:
                lines = fr.readlines()
                if len(lines) == 0:
                    raise Exception("Func: ParaInitialization, config.txt is empty")
                for line in lines:
                    tokens = re.split(' |\t|\n', line)
                    tokens = [k for k in tokens if k is not '']
                    if not len(tokens) == 2:
                        raise Exception("3 or more tokens are parsed")
                    else:
                        self.parameters[tokens[0]] = tokens[1]

    def UpdateConfigFileDir(self, dir):
        if not self.workdir == dir:
            self.workdir = dir
            print("Working Dir is Updated")

    def UpdateParameters(self, paraKey, paraValue):
        if paraKey not in self.parameters:
            raise Exception("the given parameter is not in the config.txt")
        else:
            if not self.parameters[paraKey] == paraValue:
                self.parameters[paraKey] = paraValue
                self.isParaModified = True
            else:
                pass

    def WriteToConfigFile(self):
        if not os.path.isfile(self.configfilepath):
            raise Exception("Config.txt is not exist")
        else:
            if self.isParaModified:
                with open(self.configfilepath, 'w') as fw:
                    for k, v in self.parameters.items():
                        fw.write(k)
                        fw.write("\t")
                        fw.write(v)
                        fw.write("\n")
                self.isParaModified = False
                print("The config.txt is updated")
            else:
                pass


def main():
    config = ConfigFile()
    try:
        config.UpdateParameters("data_dir", "C:你太好\qiu")
        config.UpdateParameters("com_dir", "shsdfasdi")
        # config.UpdateParameters("dfs", "s")
        config.WriteToConfigFile()
        config.UpdateParameters("com_dir", "sasdhi")
        config.WriteToConfigFile()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
