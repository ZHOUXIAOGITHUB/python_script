#-*- encoding=utf8 -*-
#Author:
#Time:  2021/9/2 14:30
#File:  man.py
from house_dictionary.test_runner import Test_Runner


class Man:
    def start_test(self):
        Test_Runner().test_runner()
if __name__ == '__main__':
    Man().start_test()