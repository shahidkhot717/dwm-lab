#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 08:55:53 2019

@author: aiktc
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing dataset
dataset=pd.read_csv('Market_Basket_Optimisation.csv',header=None)
transaction=[]
for i in range(0,7501):
    transaction.append([str(dataset.values[i,j]) for j in range(0,20)])
    
    #traninng apriori on the dataset
from apyori import apriori
rules=apriori(transaction,min_support=0.003,min_confidence=0.2,min_lift=3,min_lenght=2)

#visualizing results
results=list(rules)

results_list=[]
for i in range(0,len(results)):
    results_list.append('RULE:\t' + str(results[i][0]).replace('frozenset',' ') 
    + '\nSUPPORT:\t' + str(results[i][1]) 
    + '\nCONF:\t' + str(results[i][2][0][2]) 
    + '\nLIFT:\t' + str (results[i][2][0][3]))      