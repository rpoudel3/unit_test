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
        u = urllib2.urlopen(url)
        f = open(fname, 'w')
        f.write(u.read())
    except urllib2.URLError:
        raise ValueError('Invalid URL')

    with open(fname,'rb')as g:
        try:
                dialect=csv.Sniffer().sniff(g.read(1024))
                g.seek(0)
        except csv.Error:
            #sys.exit('file %s, line %d: %s' %(fname, reader.line_num, e))
            raise TypeError('Invalid CSV')
    g.close()
    return fname

url_to_csv('http://stackoverflow.com/questions/17730173/python-cant-get-full-path-name-of-file','fname')
    
def batch_url_to_csv(urls, fnames):
    """Takes a list of URLs to CSV files, downloads them, and 
    saves them to files given by the list of names in fnames.
    Returns a list of the filenames saved."""
    list_of_files=[]
    for i in range(len(urls)):
        try:
            list_of_files.append(url_to_csv(urls[i],fnames[i]))
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
    
    

