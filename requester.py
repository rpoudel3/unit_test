import urllib2
import csv
import sys
import pandas as pd
from io import StringIO
import warnings
import os


def url_to_csv(url, fname):
    """Takes a URL to a CSV file, downloads it, 
    and saves it to a file"""

    try:
        data = pd.read_csv(url)
        data.to_csv(fname)
    except urllib2.URLError:
        raise ValueError('Invalid URL')
    except IOError:
        raise TypeError
    except pd.parser.CParserError:
        raise TypeError('URL Cannot be Parsed as CSV')

    return  os.path.abspath('{0}.csv'.format(fname))

#url_to_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data','fname')

import itertools

def batch_url_to_csv(urls, fnames):
    """Takes a list of URLs to CSV files, downloads them, and
    saves them to files given by the list of names in fnames.
    Returns a list of the filenames saved."""
    list_of_files=[]
    reader_list=[]
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
    total_rows=0
    for j in range(len(list_of_files)):
        reader=csv.DictReader(list_of_files[j])
        for rows in reader:
            total_rows+=1
        reader_list.append(total_rows)
    print reader_list
    unique2=set((reader_list))
    if len(unique2)!=len(reader_list):
        raise AssertionError("URLS have same content")
    return list_of_files


# batch_url_to_csv(["http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data",
#              "http://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data",
#              "http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"],fnames=['travis','travis2','travis3'])


def url_to_df(url):
    """Takes a URL to a CSV file and returns the contents of the URL 
    as a Pandas DataFrame.
    """
    u =urllib2.urlopen(url)

    f1=open('fname5.csv','wb')
    f1.write(u.read())
    try:
        pd.read_csv(url)
        with open(os.path.abspath('fname5.csv'),'rb') as csvfile:
                if csv.Sniffer().has_header(csvfile.read(5000)):
                    data_frame=pd.read_csv(url, header=0)
                else:
                    data_frame=pd.read_csv(url, header=None)
    except urllib2.URLError:
                 raise ValueError('Invalid URL')
    except IOError:
                 raise TypeError
    except pd.parser.CParserError:
                 raise TypeError('URL Cannot be Parsed as CSV')
    return data_frame


