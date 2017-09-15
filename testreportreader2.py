#-------------------------------------------------------------------------------
# Name:        testreportreader2
# Purpose:     unittest module for reportreader
#
# Author:      kpchang
#
# Created:     23/07/2016
# Copyright:   (c) kpchang 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import reportreader
import unittest
import timeit

class TestReadReport (unittest.TestCase):
    """
        Testcases for reportreader.read_report
    """
    def setUp(self):
        self.filenames = []
        self.filenames.append("testfile/201321757.txt")
        self.filenames.append("testfile/201625900.txt")
        self.filenames.append("testfile/201625901.txt")
        self.filenames.append("testfile/201624672.txt")

    def test_reportreader(self):
        for item in self.filenames:
            print(reportreader.read_report(item))

def main():
    unittest.main()


if __name__ == '__main__':
    main()
