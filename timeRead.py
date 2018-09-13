# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 19:43:59 2018

@author: Mike
"""
import timeit
sc='''
import pandas as pd
c='sample2.csv'
f='sample2.por'
wid=[2,9,9,12,12,12,12,12,12]
col=[1,2,4,6,7]
'''

readFWF='''    
F=pd.read_fwf('./'+f,header=None,widths=wid,usecols=col)
'''
readCSV='''    
C=pd.read_csv('./'+c,usecols=col,header=None)
'''
t1=timeit.Timer(readFWF,sc)
t2=timeit.Timer(readCSV,sc)

print('Read fwf:')
print('{:.3f}'.format(t1.timeit(10)/10),' sec')
print()
print('Read csv:')
print('{:.3f}'.format(t2.timeit(10)/10),' sec')
print()
