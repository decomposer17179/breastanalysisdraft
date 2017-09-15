#-------------------------------------------------------------------------------
# Name:        testreadlist
# Purpose:
#
# Author:      kpchang
#
# Created:     14/03/2016
# Copyright:   (c) kpchang 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import readlist
import pathlib
import unittest
import timeit

class TestReadList(unittest.TestCase):
    def setUp(self):
        self.p = pathlib.Path("./testfile")
        self.folder = "./testfile/testfolder"
        self.zipf = "./testfile/testfolder.zip"

    def test_month(self):
        with open("./testfile/201600019.txt", "r", encoding="big5") as f:
            self.assertEqual(readlist.read_month_from_file(f), "10501")

    def test_make_dic(self):
        self.assertEqual(readlist.make_dic_from_folder(self.folder)["10501"],  ['testfile\\testfolder\\201600001.txt',
            'testfile\\testfolder\\201600002.txt', 'testfile\\testfolder\\201600003.txt', 'testfile\\testfolder\\201600004.txt'])

    def test_zip(self):
        self.assertEqual(readlist.make_dic_from_zip(self.zipf)["10501"],  ['testfolder/201600001.txt',
            'testfolder/201600002.txt', 'testfolder/201600003.txt', 'testfolder/201600004.txt'])

def main():
    unittest.main()

if __name__ == '__main__':
    main()
