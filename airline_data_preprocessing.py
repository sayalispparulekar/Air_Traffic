#Importing the Libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Importing the Dataset
dataset=pd.read_csv("Airlinewise.csv")

d=dataset.iloc[:, 5:]
a=dataset.iloc[:,:5]

X=d.loc[~(d==0).all(axis=1)]



