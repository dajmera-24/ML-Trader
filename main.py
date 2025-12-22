import numpy as np
import pandas as pd
import sys
import csv

if input('This is the GUI-less interface. Type \'Y\' if you would like to proceed, and N if you would like to exit.') == 'N':
    sys.exit()

tickers = input('Please enter the tickers you would like to look into, comma separated >>> ').split(',')
