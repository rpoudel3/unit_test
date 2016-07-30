import numpy as np
import requester
import requests
import unittest
import pandas as pd




class TestURL(unittest.TestCase):

    def test_valid_url(self):
        # Test that the function returns a filename
        url = "http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
        returned_fname = requester.url_to_csv(url, fname="test_fname.csv")
        self.assertIsInstance(returned_fname, str)
        self.assertEqual(returned_fname, "test_fname.csv")

    def test_invalid_url(self):
        invalid_url = "http://golakjsd.com/jl2kais"
        with self.assertRaises(ValueError):
            requester.url_to_csv(invalid_url,'test.csv')

    def test_valid_csv(self):
        url="http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
        readerobject=requester.url_to_csv(url, fname='/Users/rashmipoudel/Downloads/fname.csv')
        self.assertTrue(str(type(readerobject)),"_csv.reader")

    def test_invalid_csv(self):
        url="http://stackoverflow.com/questions/17730173/python-cant-get-full-path-name-of-file"
        with self.assertRaises(TypeError):
            requester.url_to_csv(url,'tester.csv')


class Test_batch_URL_csv(unittest.TestCase):
    def test_valid_url(self):

         #emits a runtime warning indicating that the invalid URL was skipped.
        url = ["http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data",
                "http://golakjsd.com/jl2kais",
               "http://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/forestfires.csv"]
        returned_fname = requester.batch_url_to_csv(url, fnames=["test_fname.csv", "test2_fname.csv","test3_fname.csv"])
        self.assertEqual(returned_fname, ["test_fname.csv","test3_fname.csv"])

    def test_number_of_files(self):
         url = ["http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data",
                "http://golakjsd.com/jl2kais",
               "http://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/forestfires.csv"]
         returned_fname=requester.batch_url_to_csv(url, fnames=["test_fname.csv", "test2_fname.csv","test3_fname.csv"])
         number_files=len(returned_fname)
         self.assertEqual(number_files, 2)

    #def test_correct_filenames(self):


    # def test_valid_batch_files(self):
    #     # ensures that the batch_url_to_csv generates the same number
    #     url = ["http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data",
    #             "http://golakjsd.com/jl2kais",
    #            "http://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/forestfires.csv"]
    #
    #     returned_fname = requester.batch_url_to_csv(url, fnames=["test_fname.csv", "test2_fname.csv","test3_fname.csv"])
    #     #self.assertIsInstance(returned_fname, str)
    #     self.assertEqual(returned_fname, ["test_fname.csv","test3_fname.csv"])



    # def test_invalid_url(self):
    #     invalid_url = "http://golakjsd.com/jl2kais"
    #     with self.assertRaises(ValueError):
    #         requester.url_to_csv(invalid_url)
    #
    # def test_valid_csv(self):
    #     url="http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data",
    #     readerobject=requester.url_to_csv(url, fname='/Users/rashmipoudel/Downloads/fname.csv')
    #     self.assertTrue(str(type(readerobject)),"_csv.reader")
    #




# class TestURL_df(unittest.TestCase):
#     def test_dataframe(self):
#         """Ensure url_to_df( ) returns a Pandas DataFrame object"""
#
#         url="http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
#         readerobject=requester.url_to_df(url)
#         self.assertIsInstance(readerobject,pd.DataFrame)
#
#     # def test_dataframe_rows(self):
    # # Ensure the number of rows in the Pandas DataFrame returned
    # # by url_to_df( ) matches the number of rows in the CSV when there is no header row in the CSV
    #
    #      url="http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
    #
    #     readerobject=requester.url_to_df(url)
    #     a=len(readerobject.index)
    #
    #
    #     self.assertEqual(a)






