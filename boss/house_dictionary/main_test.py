# -*- encoding=utf8 -*-
# Author:
# Time:  2021/7/20 11:28
# File:  main.py
from house_dictionary.element_operate import Element_Operate
from house_dictionary.house_q import Login, Operate_page
import unittest
class Main(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @classmethod
    def setUpClass(self) -> None:
        pass

    @classmethod
    def tearDownClass(self) -> None:
        pass
    def test_main(self):
        d = Element_Operate("Chrome")
        login = Login(d)
        login.login_page()
        operate = Operate_page(d)
        operate.select_house_dic()
        operate.add_house()
if __name__ == '__main__':
    unittest.main()


