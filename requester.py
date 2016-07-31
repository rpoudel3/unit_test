import urllib2
import csv
import sys
import pandas as pd
import requests
from io import StringIO
import warnings


def url_to_csv(url, fname):
    """Takes a URL to a CSV file, downloads it, 
    and saves it to a file"""

    try:
        data = pd.read_csv(url)
        data.to_csv(fname)
        #response=urllib2.urlopen(url)
        #cr=csv.reader(response)
    except urllib2.URLError:
        raise ValueError('Invalid URL')
    except IOError:
        raise TypeError
    except pd.parser.CParserError:
        raise TypeError('URL Cannot be Parsed as CSV')
    return fname

#url_to_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer/breast-cancer-data','fname')

def batch_url_to_csv(urls, fnames):
    """Takes a list of URLs to CSV files, downloads them, and 
    saves them to files given by the list of names in fnames.
    Returns a list of the filenames saved."""
    list_of_files=[]
    unique=set(urls)
    if len(unique)!=len(urls):
        raise AssertionError("Duplicate URLS cannot be present in the parameter 'urls'")
    for i in range(len(urls)):
            try:
                list_of_files.append(url_to_csv(urls[i],fnames[i]))
            except TypeError:
                    warnings.warn('RuntimeWarning,%s has been skipped' % (urls[i]))
            except ValueError:
                    warnings.warn('RuntimeWarning,%s has been skipped' % (urls[i]))
                #skip=True
                #continue
    return list_of_files

         
def url_to_df(url):
    """Takes a URL to a CSV file and returns the contents of the URL 
    as a Pandas DataFrame.
    """

    data_frame=pd.read_csv(url)
    return data_frame
    
    

