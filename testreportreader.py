#-------------------------------------------------------------------------------
# Name:        testreportreader
# Purpose:     unittest module for reportreader
#
# Author:      kpchang
#
# Created:     13/03/2016
# Copyright:   (c) kpchang 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import reportreader
import unittest
import timeit

class TakeDiagTest(unittest.TestCase):
    """
        Testcases for reportreader.take_diag_data
    """
    def setUp(self):
        self.immuline = """2. Immunohistochemical study: ER (negative, 0/4),
        PR(negative, 0/4), AR(negative, 0/4), Her2/neu(positive, score 3+),
        Ki67 proliferation index(65.5%), and EGFR(positive, +/+++, 20%)."""
        self.secondimmuline = "The immunohistochemical study for the primary invasive tumor cells(section A6):"
        self.stageline = "3. Pathologic stage: mrpT3NX, cM0, stage IIB (AJCC, 2010)."
        self.normalline = """1. Breast, 7/3, left, breast conserving surgery,
        invasive ductal carcinoma, grade 3/3 with free resection margin."""

    def take_immuline(self):
        reportreader.take_diag_data(self.secondimmuline)

    def take_stageline(self):
        reportreader.take_diag_data(self.stageline)

    def test_immuline(self):
        self.assertRaises(ValueError, self.take_immuline)

    def test_stageline(self):
        self.assertRaises(ValueError, self.take_stageline)

    def test_normalline(self):
        diag_data = reportreader.take_diag_data(self.normalline)
        print(diag_data)
        self.assertEqual(diag_data[reportreader.PROCEDURE][0], "breast conserving surgery")

class TakeIHCTest(unittest.TestCase):
    def setUp(self):
        self.report_one = reportreader.read_report("testfile/201534199draft.txt")
        self.result_one = "CK7 (negative"
        self.report_two = reportreader.read_report("testfile/201532788.txt")
        self.report_three = reportreader.read_report("testfile/201406343.txt")
        self.result_three = 'ER: positive, 4/4, 95%, evident nuclei staining, intensity and proportion: mild(35%), moderate(30%), strong(30%)'

    def test_ihc_from_desc(self):
        self.assertEqual(reportreader.take_ihc_from_desc(self.report_one)[0].strip(), self.result_one)

    def test_ihc_from_report(self):
        self.assertRaises(ValueError, self.ihc_in_empty)
        self.assertEqual(reportreader.take_ihc(self.report_three)[0], self.result_three)
        print(reportreader.take_ihc(self.report_two))

    def ihc_in_empty(self):
        emptydic = {reportreader.DIAG_COLUMN:[]}
        reportreader.take_ihc(emptydic)

def bench_normalline():
    normalline = """1. Breast, 7/3, left, breast conserving surgery,
        invasive ductal carcinoma, grade 3/3 with free resection margin."""
    reportreader.take_diag_data(normalline)

def bench_readreport():
    reportreader.read_report("testfile/201532788.txt")


def main():
    #print(timeit.timeit(bench_normalline, number = 100000))
    #print(timeit.timeit(bench_readreport, number = 10000))
    unittest.main()


if __name__ == '__main__':
    main()
