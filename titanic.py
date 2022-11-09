# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 21:41:09 2022

@author: SPTINT-02
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv('C:/Users/SPTINT-02/Downloads/train.csv')
g=sns.countplot(x='Sex',hue='Survived',data=data)