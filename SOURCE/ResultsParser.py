# -*-coding: UTF-8 -*-

import math
import os
import os.path
import re
import xml.etree.ElementTree as ET


class Result:
    def __init__self(self):
        self.data_file_name = ""
        self.reliability = 0.0
        self.v_bottleneck = [0.0] * 10

        self.t_bottleneck = [0.0] * 10
        self.l_bottleneck = [0.0] * 10
        self.v_bottleneck_index = 0
        self.t_bottleneck_index = 0
        self.l_bottleneck_index = 0


class ResultsParser:
    def __init__(self):
        result_path = "SOURCE/result"
        result_files = [f for f in os.listdir(result_path) if os.path.isfile(os.path.join(result_path, f))]
        result_files = map(lambda file: os.path.join(result_path, file), result_files)
        self.results = []

        for result_file in result_files:
            result = Result()
            tree = ET.parse(result_file)
            result.data_file_name = tree.find("data_file_name").text
            result.reliability = tree.find("reliability").text
            result.v_bottleneck, result.v_bottleneck_index = self.getBottlenecks(tree.find("bottleneck_V").text)
            result.t_bottleneck, result.t_bottleneck_index = self.getBottlenecks(tree.find("bottleneck_T").text)
            result.l_bottleneck, result.l_bottleneck_index = self.getBottlenecks(tree.find("bottleneck_L").text)
            self.results.append(result)

    def GetResults(self):
        return self.results

    def getBottlenecks(self, text):
        result = re.split(' |\t|\n|\r', text)
        max = 0
        max_index = 0
        i = 0
        for item in result:
            temp = math.fabs(float(item))
            if temp > max:
                max = temp
                max_index = i
            i += 1

        if not len(result) == 10:
            exit(-1)
        else:
            return result, max_index


