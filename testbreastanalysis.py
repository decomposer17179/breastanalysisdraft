#-------------------------------------------------------------------------------
# Name:        testbreastanalysis
# Purpose:
#
# Author:      kpchang
#
# Created:     13/03/2016
# Copyright:   (c) kpchang 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import reportreader
import breastanalysis
import breastmacro
import unittest
import timeit

class TestBreastClassify(unittest.TestCase):
    def setUp(self):
        self.reports = []
        filelist = ["201321757.txt", "201406343.txt", "201603071.txt",
                    "201530596.txt", "201532788.txt", "201534199draft.txt"]
        for filename in filelist:
            realname = "testfile/" + filename
            #print(realname)
            self.reports.append(reportreader.read_report(realname))

    def test_breast_classify(self):
        for item in self.reports:
            print(breastanalysis.breast_classify(item))



class TestIHCScoring(unittest.TestCase):
    def setUp(self):
        self.report_one = reportreader.read_report("testfile/201532788.txt")
        self.ihc_data = reportreader.take_ihc(self.report_one)
        self.report_two = reportreader.read_report("testfile/201321757.txt")
        self.ihc_data_two = reportreader.take_ihc(self.report_two)
        self.report_three = reportreader.read_report("testfile/201406343.txt")
        self.ihc_data_three = reportreader.take_ihc(self.report_three)
        self.report_four = reportreader.read_report("testfile/201401745.txt")
        self.ihc_data_four = reportreader.take_ihc(self.report_four)
        self.report_five = reportreader.read_report("testfile/201344842.txt")

    def test_percentage(self):
        target_er = breastanalysis.find_percentage(self.ihc_data[1])
        target_pr = breastanalysis.find_percentage(self.ihc_data[2])
        self.assertEqual(target_er, 98)
        self.assertEqual(target_pr, 98)
        target_er = breastanalysis.find_percentage(self.ihc_data_two[0])
        target_pr = breastanalysis.find_percentage(self.ihc_data_two[1])
        self.assertEqual(target_er, 95)
        self.assertEqual(target_pr, 90)
        target_er = breastanalysis.find_percentage(self.ihc_data_three[0])
        target_pr = breastanalysis.find_percentage(self.ihc_data_three[1])
        self.assertEqual(target_er, 95)
        self.assertEqual(target_pr, 95)
        target_er = breastanalysis.find_percentage(self.ihc_data_four[0])
        target_pr = breastanalysis.find_percentage(self.ihc_data_four[1])
        self.assertEqual(target_er, 98)
        self.assertEqual(target_pr, 25)

    def test_her2(self):
        target_her2 = breastanalysis.find_her_score(self.ihc_data[3])
        self.assertEqual(target_her2, 1)
        target_her2 = breastanalysis.find_her_score(self.ihc_data_two[2])
        self.assertEqual(target_her2, 0)
        target_her2 = breastanalysis.find_her_score(self.ihc_data_three[3])
        self.assertEqual(target_her2, 2)
        target_her2 = breastanalysis.find_her_score(self.ihc_data_four[3])
        self.assertEqual(target_her2, 1)

    def test_erprher(self):
        firstpr = breastanalysis.find_erprher(self.report_one)[breastmacro.PR]
        self.assertEqual(firstpr[1], 98)
        secondher2 = breastanalysis.find_erprher(self.report_two)[breastmacro.HERTWO]
        self.assertEqual(secondher2, 0)
        print(reportreader.take_ihc(self.report_five))

def main():
    unittest.main()

if __name__ == '__main__':
    main()
