#-*- encoding=utf8 -*-
#Author:
#Time:  2021/4/22 10:24
#File:  operate_file.py
import csv

import yaml
class Rend_File():
    # 读取yaml文件
    def read_yaml(self, file_path, username):
        """
        file_path：文件路径
        username：写入yaml文件所用的名称
        输入yaml格式:
        写入yaml文件所用的名称 :
            username : name
            password : password
        """
        with open(file_path, "r+", encoding="utf-8") as ya_file:
            ya_value = yaml.load(ya_file, Loader=yaml.FullLoader)
            return ya_value[username]

    #读取csv文件
    def read_csv(self, file_path):
        list = []
        with open(file_path, mode="r", encoding="GBK") as cs_file:
            read_file = csv.reader(cs_file)
            for cs in read_file:
                cs = cs[1]
                list.append(cs)
        return list
# tt = Rend_File().read_csv("..//house_dictionary//house_message.csv")
# print(tt)