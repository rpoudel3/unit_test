import urllib2
import csv
import sys
import pandas as pd
import requests
from io import StringIO


def url_to_csv(url, fname):
    """Takes a URL to a CSV file, downloads it, 
    and saves it to a file"""
   
    u=urllib2.urlopen(url)
    fname=open('fname.csv','w')
    fname.write(u.read())
    fname.close()
    return fname
    
def batch_url_to_csv(urls, fnames):
    """Takes a list of URLs to CSV files, downloads them, and 
    saves them to files given by the list of names in fnames.
    Returns a list of the filenames saved."""
    list_of_files=[]
    for i in range(len(urls)):
        list_of_files.append(url_to_csv(urls[i],fnames[i]))
    return list_of_files

         
def url_to_df(url):
    """Takes a URL to a CSV file and returns the contents of the URL 
    as a Pandas DataFrame.
    """
  
    data_frame=pd.read_csv(url)
    return data_frame
    
    

