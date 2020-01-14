#Importing the Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Importing the Dataset
dataset=pd.read_csv("Citypairwise.csv")
d=dataset.iloc[:, 4:]

X=d.loc[~(d==0).all(axis=1)]
