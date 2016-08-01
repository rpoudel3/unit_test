import requester
import unittest
import pandas as pd
import os




class TestURL(unittest.TestCase):
    os.getcwd()

    def test_valid_url(self):
        # test to see if the url passed in is valid.
        cwd=os.getcwd()
        url = "http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
        returned_fname = requester.url_to_csv(url, fname="test_fname.csv")
        self.assertIsInstance(returned_fname, str)
        self.assertEqual(returned_fname, "{0}/{1}.csv".format(cwd,'test_fname.csv'))

    def test_invalid_url(self):
        # test to see if the url passed in is invalid.
        invalid_url = "http://golakjsd.com/jl2kais"
        with self.assertRaises(ValueError):
            requester.url_to_csv(invalid_url,'test.csv')

    def test_valid_csv(self):
        #test to see if the valid url has a valid csv.
        url="http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
        readerobject=requester.url_to_csv(url, fname='fname.csv')
        self.assertTrue(str(type(readerobject)),"_csv.reader")

    # def test_invalid_csv(self):
    #     #test to see if the valid url has an invalid csv.
    #     url="http://stackoverflow.com/questions/17730173/python-cant-get-full-path-name-of-file"
    #     with self.assertRaises(TypeError):
    #         requester.url_to_csv(url,'/Users/rashmipoudel/Desktop/Git/unit_test/tester.csv')


class Test_batch_URL_csv(unittest.TestCase):
    # def test_valid_url(self):
    #      #emits a runtime warning indicating that the invalid CSV URL or URL that cannot be accessed was skipped.
    #
    #     url = ["http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data",
    #             "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer/breast-cancer-data",
    #            "http://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/forestfires.csv"]
    #     returned_fname = requester.batch_url_to_csv(url, fnames=["test", "test2","test3"])
    #     self.assertEqual(returned_fname, ["/Users/rashmipoudel/Desktop/Git/unit_test/test",
    #                                       "/Users/rashmipoudel/Desktop/Git/unit_test/test2",
    #                                       "/Users/rashmipoudel/Desktop/Git/unit_test/test3"])

    def test_number_of_files(self):
        #unittest no.4
         url = ["http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data",
                "http://golakjsd.com/jl2kais",
               "http://stackoverflow.com/questions/17730173/python-cant-get-full-path-name-of-file"]

         returned_fname=requester.batch_url_to_csv(url, fnames=["test_fname.csv",
                                                                "test2_fname.csv",
                                                                "test3_fname.csv"])
         number_files=len(returned_fname)
         self.assertEqual(number_files, 1)

    # def test_correct_filenames(self):
    #     #unittest no.6
    #     url = ["https://docs.travis-ci.com/user/languages/python",
    #             "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer/breast-cancer-data",
    #            "http://google.com/student"]
    #     returned_fname=requester.batch_url_to_csv(url,fnames=['t1',
    #                                                           't2',
    #                                                           't3'])
    #     self.assertEqual(returned_fname,['/Users/rashmipoudel/Desktop/Git/unit_test/t2'])

    def test_content_file(self):
        url=["http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data",
             "http://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data",
             "http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"]

        with self.assertRaises(AssertionError):
            requester.batch_url_to_csv(url,fnames=['m1','m2','m3'])




    # def test_correct_number_of_filenames(self):
    #     #unittest no.7
    #     url = ["https://docs.travis-ci.com/user/languages/python",
    #             "https://github.com/pydata/pandas/issues/10153",
    #            "http://stackoverflow.com/questions/17730173/python-cant-get-full-path-name-of-file"]
    #
    #     returned_fname=requester.batch_url_to_csv(url, fnames=["test_fname.csv",
    #                                                            "test2_fname.csv",
    #                                                            "test3_fname.csv"])
    #     number_files=len(returned_fname)
    #     self.assertEqual(number_files, 0)

    def test_duplicate_URLS(self):
        #unittest no.8
        url = ["https://docs.travis-ci.com/user/languages/python",
                "https://github.com/pydata/pandas/issues/10153",
               "https://github.com/pydata/pandas/issues/10153"]
        with self.assertRaises(AssertionError):
            requester.batch_url_to_csv(url,fnames=['travis','travis2','travis3'])

class TestURL_df(unittest.TestCase):
    def test_dataframe(self):
        """Ensure url_to_df( ) returns a Pandas DataFrame object"""

        url="http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
        readerobject=requester.url_to_df(url)
        self.assertIsInstance(readerobject,pd.DataFrame)

    def test_number_of_rows_without_header(self):
        url="http://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data"

        reader=requester.url_to_df(url)
        rows,columns=reader.shape
        self.assertEqual(rows,1728)

    def test_number_of_rows_with_header(self):
         url="http://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/forestfires.csv"

         reader=requester.url_to_df(url)
         rows,columns=reader.shape
         self.assertEqual(rows,517)


    # def test_dataframe_rows(self):
    # Ensure the number of rows in the Pandas DataFrame returned
    # by url_to_df( ) matches the number of rows in the CSV when there is no header row in the CSV

        #  url="http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
        #
        # readerobject=requester.url_to_df(url)
        # a=len(readerobject.index)








